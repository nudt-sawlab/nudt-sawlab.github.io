from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RESEARCH_TEMPLATE = ROOT / "layouts/partials/widgets/research.html"
PUBLICATIONS_TEMPLATE = ROOT / "layouts/partials/widgets/publications.html"

TARGET_PUBLICATIONS = {
    "content/en/publication/PiLoT_2026/index.md": "content/en/publication/PiLoT_2026/teaser.png",
    "content/en/publication/SpectralMoE_2026/index.md": "content/en/publication/SpectralMoE_2026/teaser.png",
    "content/en/publication/SensLoc_2023/index.md": "content/en/publication/SensLoc_2023/teaser.png",
    "content/en/publication/Render2Loc_2023/index.md": "content/en/publication/Render2Loc_2023/teaser.png",
    "content/en/publication/S2AMSnet_2024/index.md": "content/en/publication/S2AMSnet_2024/teaser.png",
    "content/en/publication/NTR-Gaussian_2025/index.md": "content/en/publication/NTR-Gaussian_2025/teaser.png",
    "content/en/publication/DeepAC_2023/index.md": "content/en/publication/DeepAC_2023/teaser.gif",
    "content/en/publication/LoDLoc_2024/index.md": "content/en/publication/LoDLoc_2024/teaser.gif",
    "content/en/publication/LoDLoc2_2025/index.md": "content/en/publication/LoDLoc2_2025/teaser.gif",
    "content/en/publication/UAVD4L_2024/index.md": "content/en/publication/UAVD4L_2024/teaser.gif",
}


def test_research_template_supports_research_specific_media_override():
    content = RESEARCH_TEMPLATE.read_text(encoding="utf-8")
    assert "research_media_icon" in content


def test_publications_template_supports_research_specific_media_override():
    content = PUBLICATIONS_TEMPLATE.read_text(encoding="utf-8")
    assert "research_media_icon" in content


def test_target_publications_use_final_media_icon_without_override():
    for index_path, asset_path in TARGET_PUBLICATIONS.items():
        front_matter = (ROOT / index_path).read_text(encoding="utf-8")
        assert "research_media_icon:" not in front_matter, index_path
        assert f'src: "{Path(asset_path).name}"' in front_matter, index_path


def test_research_override_assets_exist():
    for asset_path in TARGET_PUBLICATIONS.values():
        assert (ROOT / asset_path).exists(), asset_path
