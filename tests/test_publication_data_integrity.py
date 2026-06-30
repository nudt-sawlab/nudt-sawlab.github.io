from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION_ROOT = ROOT / "content/en/publication"
RESEARCH_PAGE = ROOT / "content/en/home/research.md"

ECCV_2026_PUBLICATIONS = {
    "AV2T-Gen: Aerial Visible to Thermal Generation with Environment and Vehicle State Guidance": {
        "publication": PUBLICATION_ROOT / "AV2T-Gen_2026/index.md",
        "news": ROOT / "content/en/news/eccv-260627-av2t-gen/index.md",
        "news_title": "AV2T-Gen accepted by ECCV 2026.",
    },
    "ThermoGS: Decoupling Physical Surface Attributes for Spatio-Temporal Thermal Field Emulation via 4D Gaussian Splatting": {
        "publication": PUBLICATION_ROOT / "ThermoGS_2026/index.md",
        "news": ROOT / "content/en/news/eccv-260627-thermogs/index.md",
        "news_title": "ThermoGS accepted by ECCV 2026.",
    },
}


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    _, data, _ = text.split("---", 2)
    return yaml.safe_load(data) or {}


def resolve_publication_media_paths(pub_dir, media_icon):
    src = media_icon.get("src", "")
    if not src:
        return []

    paths = [pub_dir / src]
    src_lower = src.lower()
    if (
        media_icon.get("type", "image") == "video"
        or src_lower.endswith(".webm")
        or src_lower.endswith(".mp4")
    ):
        stem = Path(src).with_suffix("")
        paths.append(pub_dir / f"{stem}.png")

    return paths


def publication_front_matters():
    for index_path in sorted(PUBLICATION_ROOT.glob("*/index.md")):
        yield index_path, front_matter(index_path)


def test_publication_media_references_exist():
    missing = []
    for index_path, data in publication_front_matters():
        pub_dir = index_path.parent
        for key in ("media_icon", "research_media_icon"):
            media_icon = data.get(key)
            if not media_icon:
                continue
            for media_path in resolve_publication_media_paths(pub_dir, media_icon):
                if not media_path.exists():
                    missing.append(f"{index_path.relative_to(ROOT)} {key}: {media_path.relative_to(ROOT)}")

    assert not missing, "Missing publication media assets:\n" + "\n".join(missing)


def test_spectralmoe_publication_uses_project_teaser():
    publication_teaser = ROOT / "content/en/publication/SpectralMoE_2026/teaser.png"
    project_teaser = ROOT / "static/SpectralMoE/static/images/teaser.png"

    assert publication_teaser.read_bytes() == project_teaser.read_bytes()


def test_new_eccv_2026_publications_have_empty_paper_links_and_matching_news():
    research_entries = {
        entry["title"]: entry
        for entries in front_matter(RESEARCH_PAGE)["research_step_papers"].values()
        for entry in entries
    }

    for title, paths in ECCV_2026_PUBLICATIONS.items():
        publication = front_matter(paths["publication"])
        research_entry = research_entries[title]
        news = front_matter(paths["news"])

        assert publication["journal"] == "ECCV 2026"
        assert research_entry["journal"] == "ECCV 2026"
        assert news["title"] == paths["news_title"]
        assert "Preprint" not in paths["news"].read_text(encoding="utf-8")

        publication_paper = next(link for link in publication["links"] if link["name"] == "Paper")
        research_paper = next(link for link in research_entry["links"] if link["name"] == "Paper")

        assert publication_paper["url"] == ""
        assert research_paper["url"] == ""


def test_authors_text_has_no_repeated_spaces():
    errors = []
    for index_path, data in publication_front_matters():
        authors_text = data.get("authors_text", "")
        if "  " in authors_text:
            errors.append(f"{index_path.relative_to(ROOT)}: {authors_text}")

    for step, research_entries in front_matter(RESEARCH_PAGE)["research_step_papers"].items():
        for entry in research_entries:
            authors_text = entry.get("authors_text", "")
            if "  " in authors_text:
                errors.append(f"{RESEARCH_PAGE.relative_to(ROOT)} {step} {entry['title']}: {authors_text}")

    assert not errors, "Repeated spaces in authors_text:\n" + "\n".join(errors)


@pytest.mark.parametrize(
    "research_entry",
    front_matter(RESEARCH_PAGE)["research_step_papers"]["step1"]
    + front_matter(RESEARCH_PAGE)["research_step_papers"]["step2"]
    + front_matter(RESEARCH_PAGE)["research_step_papers"]["step3"],
    ids=lambda entry: entry["title"],
)
def test_research_authors_match_publication_authors(research_entry):
    publications = {
        data["title"]: data
        for _, data in publication_front_matters()
        if "title" in data
    }

    title = research_entry["title"]
    assert title in publications
    assert research_entry["authors_text"] == publications[title]["authors_text"]
