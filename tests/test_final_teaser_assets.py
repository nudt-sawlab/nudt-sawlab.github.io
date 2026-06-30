from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION_ROOT = ROOT / "content/en/publication"
RESEARCH_PAGE = ROOT / "content/en/home/research.md"
FINAL_TEASER_ROOT = ROOT / "teaser"
RESEARCH_ASSET_ROOT = ROOT / "static/img/research"


FINAL_TEASERS = {
    "3-D Thermal_2026": ("3D-Thermal.png", "teaser.png"),
    "AV2T-Gen_2026": ("AV2T-Gen.png", "teaser.png"),
    "AerialExtreMatch_2026": ("AerialExtreMatch.png", "teaser.png"),
    "AirZoo_2026": ("AirZoo.jpg", "teaser.jpg"),
    "Cross-SPECL_2026": ("Cross-SPECL.png", "teaser.png"),
    "DeepAC_2023": ("DeepAC.gif", "teaser.gif"),
    "FCP-SatMVS_2026": ("FCP-SatMVS.webp", "teaser.webp"),
    "LoD-Locv3_2026": ("LoD-Loc-v3.png", "teaser.png"),
    "LoDLoc2_2025": ("LoD-Loc-v2.gif", "teaser.gif"),
    "LoDLoc_2024": ("LoD-Loc.gif", "teaser.gif"),
    "NGC-GeoLoc_2026": ("NGC-GeoLoc.png", "teaser.png"),
    "NTR-Gaussian_2025": ("NTR-Gaussian.png", "teaser.png"),
    "PiLoT_2026": ("PiLoT.png", "teaser.png"),
    "Render2Loc_2023": ("Render2Loc.png", "teaser.png"),
    "S2AMSnet_2024": ("S2AMSnet.png", "teaser.png"),
    "SensLoc_2023": ("SensLoc.png", "teaser.png"),
    "SpectralMoE_2026": ("SpectralMoE.png", "teaser.png"),
    "TGRS_20240110": ("ATLoc.png", "teaser.png"),
    "TGRS_20240429": ("Target-Detection.png", "teaser.png"),
    "ThermalGS_2025": ("ThermalGS.gif", "teaser.gif"),
    "ThermoGS_2026": ("ThermoGS.png", "teaser.png"),
    "UAV-GeoLoc-2025": ("UAV-GeoLoc.gif", "teaser.gif"),
    "UAVD4L_2024": ("UAVD4L.gif", "teaser.gif"),
}


RESEARCH_TEASERS = {
    "UAV-GeoLoc: A Large-vocabulary Dataset and Geometry-Transformed Method for UAV Geo-Localization": "UAV-GeoLoc.gif",
    "AerialExtreMatch: A Benchmark for Extreme-View Image Matching and Localization": "AerialExtreMatch.png",
    "LoD-Loc v2: Aerial Visual Localization over Low Level-of-Detail City Models using Explicit Silhouette Alignment": "LoD-Loc-v2.gif",
    "LoD-Loc: Aerial Visual Localization using LoD 3D Map with Neural Wireframe Alignment": "LoD-Loc.gif",
    "UAVD4L:A Large-Scale Dataset for UAV 6-DoF Localization": "UAVD4L.gif",
    "ATLoc: Aerial Thermal Images Localization via View Synthesis": "ATLoc.png",
    "Deep Active Contours for Real-time 6-DoF Object Tracking": "DeepAC.gif",
    "Render-and-compare: Cross-view 6-dof localization from noisy prior": "Render2Loc.png",
    "Long-term Visual Localization with Mobile Sensors": "SensLoc.png",
    "PiLoT: Neural Pixel-to-3D Registration for UAV-based Ego and Target Geo-localization": "PiLoT.png",
    "AirZoo: A Unified Large-Scale Dataset for Grounding Aerial Geometric 3D Vision": "AirZoo.jpg",
    "NGC-GeoLoc: Neural GeoCoordinate Regression for GPS-Denied UAV Geo-Localization": "NGC-GeoLoc.png",
    "LoD-Loc v3: Generalized Aerial Localization in Dense Cities using Instance Silhouette Alignment": "LoD-Loc-v3.png",
    "Spectral–spatial Adversarial Multidomain Synthesis Network for Cross-scene Hyperspectral Image Classification": "S2AMSnet.png",
    "Target Detection With Spectral Graph Contrast Clustering Assignment and Spectral Graph Transformer in Hyperspectral Imagery": "Target-Detection.png",
    "Local Precise Refinement: A Dual-Gated Mixture-of-Experts for Enhancing Foundation Model Generalization against Spectral Shifts": "SpectralMoE.png",
    "FCP-SatMVS: Feature-Context-Progressive Network for Robust Satellite Digital Surface Model": "FCP-SatMVS.webp",
    "Cross-SPECL: Cross-Scene Hyperspectral Image Classification via Spectral Stability Exploiting and Causal Learning": "Cross-SPECL.png",
    "ThermoGS: Decoupling Physical Surface Attributes for Spatio-Temporal Thermal Field Emulation via 4D Gaussian Splatting": "ThermoGS.png",
    "AV2T-Gen: Aerial Visible to Thermal Generation with Environment and Vehicle State Guidance": "AV2T-Gen.png",
    "NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics": "NTR-Gaussian.png",
    "3-D Thermal City Reconstruction via Thermal Mapping With RGB-Mesh Guidance": "3D-Thermal.png",
    "ThermalGS: Dynamic 3D Thermal Reconstruction with Gaussian Splatting": "ThermalGS.gif",
}


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    _, data, _ = text.split("---", 2)
    return yaml.safe_load(data) or {}


def research_entries():
    data = front_matter(RESEARCH_PAGE)
    for entries in data["research_step_papers"].values():
        yield from entries


def test_publication_media_uses_final_teaser_assets():
    for pub_dir_name, (review_name, publication_name) in FINAL_TEASERS.items():
        pub_dir = PUBLICATION_ROOT / pub_dir_name
        data = front_matter(pub_dir / "index.md")
        media_icon = data["media_icon"]
        expected_publication_asset = pub_dir / publication_name
        expected_review_asset = FINAL_TEASER_ROOT / review_name

        assert media_icon["type"] == "image"
        assert media_icon["src"] == publication_name
        assert "research_media_icon" not in data
        assert expected_publication_asset.read_bytes() == expected_review_asset.read_bytes()


def test_research_entries_use_final_static_teaser_assets():
    entries_by_title = {entry["title"]: entry for entry in research_entries()}

    for title, review_name in RESEARCH_TEASERS.items():
        entry = entries_by_title[title]
        static_asset = RESEARCH_ASSET_ROOT / review_name
        review_asset = FINAL_TEASER_ROOT / review_name

        assert entry["media_icon"]["type"] == "image"
        assert entry["media_icon"]["src"] == f"img/research/{review_name}"
        assert static_asset.read_bytes() == review_asset.read_bytes()


def test_gif_teasers_render_as_images_without_poster_fallback():
    for path in (
        ROOT / "layouts/partials/widgets/research.html",
        ROOT / "layouts/partials/widgets/publications.html",
    ):
        content = path.read_text(encoding="utf-8")
        assert 'strings.HasSuffix $media_src_lower ".gif"' not in content


def test_teaser_image_wrappers_have_no_background_fill():
    content = (ROOT / "assets/scss/custom.scss").read_text(encoding="utf-8")
    pub_image_wrap = content.split(".pub-image-wrap {", 1)[1].split("\n}", 1)[0]

    assert "background: transparent" in pub_image_wrap
    assert "background-color:" not in pub_image_wrap
