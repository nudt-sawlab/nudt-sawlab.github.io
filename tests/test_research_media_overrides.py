from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RESEARCH_TEMPLATE = ROOT / "layouts/partials/widgets/research.html"

TARGET_PUBLICATIONS = {
    "content/en/publication/PiLoT_2026/index.md": "content/en/publication/PiLoT_2026/research-card.png",
    "content/en/publication/SpectralMoE_2026/index.md": "content/en/publication/SpectralMoE_2026/research-card.png",
    "content/en/publication/SensLoc_2023/index.md": "content/en/publication/SensLoc_2023/research-card.png",
    "content/en/publication/Render2Loc_2023/index.md": "content/en/publication/Render2Loc_2023/research-card.png",
    "content/en/publication/S2AMSnet_2024/index.md": "content/en/publication/S2AMSnet_2024/research-card.png",
    "content/en/publication/NTR-Gaussian_2025/index.md": "content/en/publication/NTR-Gaussian_2025/research-card.png",
    "content/en/publication/DeepAC_2023/index.md": "content/en/publication/DeepAC_2023/research-card.png",
    "content/en/publication/LoDLoc_2024/index.md": "content/en/publication/LoDLoc_2024/research-card.webm",
    "content/en/publication/LoDLoc2_2025/index.md": "content/en/publication/LoDLoc2_2025/research-card.webm",
    "content/en/publication/UAVD4L_2024/index.md": "content/en/publication/UAVD4L_2024/research-card.mp4",
}


def test_research_template_supports_research_specific_media_override():
    content = RESEARCH_TEMPLATE.read_text(encoding="utf-8")
    assert "research_media_icon" in content


def test_target_publications_define_research_media_override():
    for index_path in TARGET_PUBLICATIONS:
        front_matter = (ROOT / index_path).read_text(encoding="utf-8")
        assert "research_media_icon:" in front_matter, index_path


def test_research_override_assets_exist():
    for asset_path in TARGET_PUBLICATIONS.values():
        assert (ROOT / asset_path).exists(), asset_path
