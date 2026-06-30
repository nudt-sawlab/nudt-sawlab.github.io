from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TEMPLATE_PATHS = [
    ROOT / "layouts/partials/widgets/research.html",
    ROOT / "layouts/partials/widgets/publications.html",
]

POSTER_EXPECTATIONS = {
    "static/img/research/teaser_UAVGeoLoc.gif": "static/img/research/teaser_UAVGeoLoc.png",
    "static/img/research/teaser_LoDLocv2.gif": "static/img/research/teaser_LoDLocv2.png",
    "static/img/research/teaser_LoDLoc.gif": "static/img/research/teaser_LoDLoc.png",
    "static/img/research/teaser_UAVD4L.gif": "static/img/research/teaser_UAVD4L.png",
    "static/img/research/teaser_DeepAC.gif": "static/img/research/teaser_DeepAC.png",
    "static/img/research/teaser_ThermalGS.gif": "static/img/research/teaser_ThermalGS.png",
    "content/en/publication/UAV-GeoLoc-2025/demo_small.gif": "content/en/publication/UAV-GeoLoc-2025/demo_small.png",
    "content/en/publication/LoDLoc_2024/LoD_Loc.gif": "content/en/publication/LoDLoc_2024/LoD_Loc.png",
    "content/en/publication/LoDLoc2_2025/Lod_Locv2_3.gif": "content/en/publication/LoDLoc2_2025/Lod_Locv2_3.png",
    "content/en/publication/UAVD4L_2024/demo_small.gif": "content/en/publication/UAVD4L_2024/demo_small.png",
    "content/en/publication/DeepAC_2023/teaser.gif": "content/en/publication/DeepAC_2023/teaser.png",
    "content/en/publication/ThermalGS_2025/ThermalGS.gif": "content/en/publication/ThermalGS_2025/ThermalGS.png",
    "content/en/publication/LoDLoc_2024/research-card.webm": "content/en/publication/LoDLoc_2024/research-card.png",
    "content/en/publication/LoDLoc2_2025/research-card.webm": "content/en/publication/LoDLoc2_2025/research-card.png",
    "content/en/publication/UAVD4L_2024/research-card.mp4": "content/en/publication/UAVD4L_2024/research-card.png",
}


def test_teaser_templates_use_posters_and_no_preload():
    for path in TEMPLATE_PATHS:
        content = path.read_text(encoding="utf-8")
        assert "poster=" in content, path
        assert 'preload="none"' in content, path


def test_static_teaser_images_do_not_lazy_load():
    for path in TEMPLATE_PATHS:
        content = path.read_text(encoding="utf-8")
        for line in content.splitlines():
            if "<img" in line:
                assert 'loading="lazy"' not in line, path


def test_teaser_images_fit_fixed_height_without_crop():
    content = (ROOT / "assets/scss/custom.scss").read_text(encoding="utf-8")
    assert ".pub-image-wrap" in content
    assert "height: 110px;" in content
    assert "width: 200px;" in content
    assert "flex: 0 0 200px;" in content
    assert "overflow: visible;" in content
    assert "object-fit: contain;" in content


def test_teaser_titles_have_desktop_spacing_from_images():
    content = (ROOT / "assets/scss/custom.scss").read_text(encoding="utf-8")
    pub_content_wrap = content.split(".pub-content-wrap {", 1)[1].split("\n}", 1)[0]
    mobile_content = content.split("@media (max-width: 640px)", 1)[1]

    assert "padding-left: 1rem;" in pub_content_wrap
    assert ".pub-content-wrap" in mobile_content
    assert "padding-left: 0;" in mobile_content


def test_teaser_poster_assets_exist():
    for _, poster_path in POSTER_EXPECTATIONS.items():
        assert (ROOT / poster_path).exists(), poster_path


def test_fcp_satmvs_uses_compressed_teaser_asset():
    front_matter = (ROOT / "content/en/publication/FCP-SatMVS_2026/index.md").read_text(
        encoding="utf-8"
    )
    asset = ROOT / "content/en/publication/FCP-SatMVS_2026/teaser.webp"

    assert 'src: "teaser.webp"' in front_matter
    assert asset.exists()
    assert asset.stat().st_size < 600_000
