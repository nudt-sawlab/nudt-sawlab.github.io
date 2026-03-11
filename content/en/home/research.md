---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: research

active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 40

title: Research Summary
subtitle:

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.


design:
  columns: 1
  
  
  
research_step_names:

  step1: GPS-Independent UAV Localization
  step2: Planet-Scale Digital Twins
  step3: Physics-Based Multimodal Simulation

    
    
    
research_step_papers:
  step1:

    - title: "UAV-GeoLoc: A Large-vocabulary Dataset and Geometry-Transformed Method for UAV Geo-Localization"
      authors_text: "Rouwan Wu, Jiacheng Deng, Mingyu Mou, Xingyi He, Maojun Zhang, Yu Liu, **Shen Yan**"
      media_icon:
        type: image
        src: "img/research/teaser_UAVGeoLoc.gif"
      journal: "RA-L 2025"
      intro: "World-UAV -- a diverse and realistic dataset for UAV-to-satellite geo-localization, UAVPlace -- a transformation-invariant retrieval method that significantly improves performance under extreme viewpoint variations."
      cite_text: |
        @ARTICLE{11077664,
          author={Wu, Rouwan and Deng, Jiacheng and Mou, Mingyu and He, Xingyi and Zhang, Maojun and Liu, Yu and Yan, Shen},
          journal={IEEE Robotics and Automation Letters},
          title={UAV-GeoLoc: A Large-vocabulary Dataset and Geometry-Transformed Method for UAV Geo-Localization},
          year={2025},
          volume={},
          number={},
          pages={1-8},
          keywords={Autonomous aerial vehicles;Satellites;Urban areas;Satellite images;Training;Drones;Location awareness;Large language models;Engines;Data mining;Localization;recognition;vision-based navigation},
          doi={10.1109/LRA.2025.3588061}}

      links:
          - name: Paper
            url: "https://ieeexplore.ieee.org/document/11077664"

          - name: Code
            url: "https://github.com/RingoWRW/GeoLoc-UAV"

    - title: "LoD-Loc v2: Aerial Visual Localization over Low Level-of-Detail City Models using Explicit Silhouette Alignment"
      authors_text: "Juelin Zhu, Shuaibang Peng, Long Wang, Hanlin Tan, Yu Liu, Maojun  Zhang, **Shen  Yan**"
      media_icon:
        type: image
        src: "img/research/teaser_LoDLocv2.gif"
      journal: "ICCV 2025"
      intro: "A novel method for aerial visual localization over low Level-of-Detail (LoD) city models. "
      cite_text: |
        @inproceedings{zhu2025lod,
          title={LoD-Loc v2: Aerial Visual Localization over Low Level-of-Detail City Models using Explicit Silhouette Alignment},
          author={Zhu, Juelin and Yan, Shen and Wang, Long and Zhang, Shengyue and Liu, Yu and Zhang, Maojun},
          booktitle={},
          pages={},
          year={2025}
        }

      links:
          - name: Paper
            url: "https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_LoD-Loc_v2_Aerial_Visual_Localization_over_Low_Level-of-Detail_City_Models_ICCV_2025_paper.pdf"

          - name: Project Page
            url: "https://pppppsb.github.io/LoD-Locv2/"

          - name: Code
            url: "https://github.com/VictorZoo/LoD-Loc-v2"

    - title: "LoD-Loc: Aerial Visual Localization using LoD 3D Map with Neural Wireframe Alignment"
      authors_text: "Juelin Zhu*, Shen Yan*, Long Wang, Shengyue Zhang, Yu Liu, **Maojun Zhang**"
      media_icon:
        type: image
        src: "img/research/teaser_LoDLoc.gif"
      journal: "NeurIPS 2024"
      intro: ""
      cite_text: |
        @inproceedings{zhu2024lod,
          title={LoD-Loc: aerial visual localization using LoD 3D map with neural wireframe alignment},
          author={Zhu, Juelin and Yan, Shen and Wang, Long and Zhang, Shengyue and Liu, Yu and Zhang, Maojun},
          booktitle={Proceedings of the 38th International Conference on Neural Information Processing Systems},
          pages={119063--119098},
          year={2024}
        }

      links:
          - name: Paper
            url: "https://arxiv.org/abs/2410.12269"

          - name: Project Page
            url: "https://victorzoo.github.io/LoD-Loc.github.io/"

          - name: Code
            url: "https://github.com/VictorZoo/LoD-Loc"

    - title: "UAVD4L:A Large-Scale Dataset for UAV 6-DoF Localization"
      authors_text: "Rouwan Wu*, Xiaoya Cheng*, Juelin Zhu, Yuxiang Liu, Maojun Zhang†, Shen Yan"
      media_icon:
        type: image
        src: "img/research/teaser_UAVD4L.gif"
      journal: "3DV 2024"
      intro: "The first large-scale dataset designed specifically for 6-DoF localization of UAVs in GPS-denied environments"
      cite_text: |
        @inproceedings{wu2024uavd4l,
          title={UAVD4L: A Large-Scale Dataset for UAV 6-DoF Localization},
          author={Wu, Rouwan and Cheng, Xiaoya and Zhu, Juelin and Liu, Yuxiang and Zhang, Maojun and Yan, Shen},
          booktitle={2024 International Conference on 3D Vision (3DV)},
          pages={1574--1583},
          year={2024},
          organization={IEEE}
        }


      links:
          - name: Paper
            url: "https://arxiv.org/pdf/2401.05971"

          - name: Code
            url: "https://github.com/RingoWRW/UAVD4L"

    - title: "ATLoc: Aerial Thermal Images Localization via View Synthesis"
      authors_text: "Yuxiang Liu*, Rouwan Wu*, Shen Yan, Xiaoya Cheng, Juelin Zhu, Yu Liu, Maojun Zhang†"
      media_icon:
        type: image
        src: "img/research/teaser_ATLoc.png"
      journal: "TGRS 2024"
      intro: " This paper addresses the challenging problem of cross-view 6-DoF localization for thermal images by proposing a \"Render-and-Compare\" framework."
      cite_text: |
        @ARTICLE{10387530,
          author={Liu, Yuxiang and Wu, Rouwan and Yan, Shen and Cheng, Xiaoya and Zhu, Juelin and Liu, Yu and Zhang, Maojun},
          journal={IEEE Transactions on Geoscience and Remote Sensing},
          title={ATLoc: Aerial Thermal Images Localization via View Synthesis},
          year={2024},
          volume={62},
          number={},
          pages={1-13},
          keywords={Location awareness;Cameras;Three-dimensional displays;Solid modeling;6-DOF;Atmospheric modeling;Visualization;Aerial localization;thermal image;view synthesis},
          doi={10.1109/TGRS.2024.3352421}}

      links:
          - name: Paper
            url: "https://ieeexplore.ieee.org/abstract/document/10387530"

          - name: Code
            url: "https://github.com/RingoWRW/ATLoc"

    - title: "Deep Active Contours for Real-time 6-DoF Object Tracking"
      authors_text: "Long Wang*, Shen Yan*, Jianan Zhen, Yu Liu, Maojun Zhang, Guofeng Zhang, Xiaowei Zhou†"
      media_icon:
        type: image
        src: "img/research/teaser_DeepAC.gif"
      journal: "ICCV 2023"
      intro: "A real-time 6-DoF object tracking framework that integrates deep learning with active contour models to achieve robust pose estimation from monocular video."
      cite_text: |
        @inproceedings{wang2023deep,
          title={Deep active contours for real-time 6-DoF object tracking},
          author={Wang, Long and Yan, Shen and Zhen, Jianan and Liu, Yu and Zhang, Maojun and Zhang, Guofeng and Zhou, Xiaowei},
          booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
          pages={14034--14044},
          year={2023}
        }

      links:
          - name: Paper
            url: "https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_Deep_Active_Contours_for_Real-time_6-DoF_Object_Tracking_ICCV_2023_paper.pdf"

          - name: Project Page
            url: "https://zju3dv.github.io/deep_ac/"

          - name: Code
            url: "https://github.com/WangLongZJU/DeepAC"

    - title: "Render-and-compare: Cross-view 6-dof localization from noisy prior"
      authors_text: "Shen Yan, Xiaoya Cheng, Yuxiang Liu, Juelin Zhu, Rouwan Wu, Yu Liu, Maojun Zhang†"
      media_icon:
        type: image
        src: "img/research/teaser_Render2Loc.png"
      journal: "ICME 2023"
      intro: "An iterative framework that refines a noisy initial pose by matching rendered synthetic views with actual query images to bridge the geometric gap between aerial and ground perspectives."
      cite_text: |
        @inproceedings{yan2023render,
          title={Render-and-compare: Cross-view 6-dof localization from noisy prior},
          author={Yan, Shen and Cheng, Xiaoya and Liu, Yuxiang and Zhu, Juelin and Wu, Rouwan and Liu, Yu and Zhang, Maojun},
          booktitle={2023 IEEE International Conference on Multimedia and Expo (ICME)},
          pages={2171--2176},
          year={2023},
          organization={IEEE}
        }

      links:
          - name: Paper
            url: "https://arxiv.org/pdf/2302.06287.pdf"

          - name: Code
            url: "https://github.com/Choyaa/Render2Loc"

    - title: "Long-term Visual Localization with Mobile Sensors"
      authors_text: "Shen Yan, Yu Liu, Long Wang, Zehong Shen, Zhen Peng, Haomin Liu, Maojun Zhang, Guofeng Zhang, Xiaowei Zhou†"
      media_icon:
        type: image
        src: "img/research/teaser_SensLoc.png"
      journal: "CVPR 2023"
      intro: "Addresses extreme seasonal and structural appearance changes by tightly fusing visual information with standard mobile sensor data (GPS, compass, gravity)."
      cite_text: |
        @inproceedings{yan2023long,
          title={Long-term Visual Localization with Mobile Sensors},
          author={Yan, Shen and Liu, Yu and Wang, Long and Shen, Zehong and Peng, Zhen and Liu, Haomin and Zhang, Maojun and Zhang, Guofeng and Zhou, Xiaowei},
          booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
          pages={17245--17255},
          year={2023}
        }

      links:
          - name: Paper
            url: "https://openaccess.thecvf.com/content/CVPR2023/papers/Yan_Long-Term_Visual_Localization_With_Mobile_Sensors_CVPR_2023_paper.pdf"

          - name: Project Page
            url: "https://zju3dv.github.io/sensloc/"

    
  step2:

    - title: "Spectral–spatial Adversarial Multidomain Synthesis Network for Cross-scene Hyperspectral Image Classification"
      authors_text: "Xi Chen, Lin Gao, Maojun Zhang†, Chen Chen, Shen Yan"
      media_icon:
        type: image
        src: "img/research/teaser_S2AMSnet.png"
      journal: "TGRS 2024"
      intro: "A Method for Robust Cross-Scene Hyperspectral Image Classification via Expansion of Source Domain Distribution Diversity."
      cite_text: |
        @article{chen2024spectral,
          title={Spectral--spatial adversarial multidomain synthesis network for cross-scene hyperspectral image classification},
          author={Chen, Xi and Gao, Lin and Zhang, Maojun and Chen, Chen and Yan, Shen},
          journal={IEEE Transactions on Geoscience and Remote Sensing},
          volume={62},
          pages={1--16},
          year={2024},
          publisher={IEEE}
        }

      links:
          - name: Paper
            url: "https://ieeexplore.ieee.org/abstract/document/10531019"

          - name: Code
            url: "https://github.com/daxichen/S2AMSnet"


    - title: "Target Detection With Spectral Graph Contrast Clustering Assignment and Spectral Graph Transformer in Hyperspectral Imagery"
      authors_text: "Xi Chen, Maojun Zhang†, Yu Liu"
      media_icon:
        type: image
        src: "img/research/teaser_TGRS_Target.png"
      journal: "TGRS 2024"
      intro: "A Method for Hyperspectral Image Target Detection."
      cite_text: |
        @article{chen2024target,
          title={Target detection with spectral graph contrast clustering assignment and spectral graph transformer in hyperspectral imagery},
          author={Chen, Xi and Zhang, Maojun and Liu, Yu},
          journal={IEEE Transactions on Geoscience and Remote Sensing},
          volume={62},
          pages={1--16},
          year={2024},
          publisher={IEEE}
        }

      links:
          - name: Paper
            url: "https://ieeexplore.ieee.org/abstract/document/10509725"
    
  step3:
  
    - title: "NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics"
      authors_text: "Kun Yang*, Yuxiang Liu*, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang†"
      media_icon:
        type: image
        src: "img/research/teaser_NTRGaussian.png"
      journal: "CVPR 2025"
      cite_text: |
        @inproceedings{yang2025ntr,
          title={NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics},
          author={Yang, Kun and Liu, Yuxiang and Cui, Zeyu and Liu, Yu and Zhang, Maojun and Yan, Shen and Wang, Qing},
          booktitle={Proceedings of the Computer Vision and Pattern Recognition Conference},
          pages={691--700},
          year={2025}
        }
      
      links:
          - name: Paper
            url: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_NTR-Gaussian_Nighttime_Dynamic_Thermal_Reconstruction_with_4D_Gaussian_Splatting_Based_CVPR_2025_paper.pdf"
        
          - name: Code
            url: "https://github.com/NPU-CVPG/NTR-Gaussian"
    
    - title: "ThermalGS: Dynamic 3D Thermal Reconstruction with Gaussian Splatting"
      authors_text: "Yuxiang Liu, Xi Chen, Shen Yan, Zeyu Cui, Huaxin Xiao, Yu Liu, Maojun Zhang†"
      media_icon:
        type: image
        src: "img/research/teaser_ThermalGS.gif"
      journal: "Remote Sensing 2025"
      cite_text: |
        @article{thermalgs2025,
        AUTHOR = {Liu, Yuxiang and Chen, Xi and Yan, Shen and Cui, Zeyu and Xiao, Huaxin and Liu, Yu and Zhang, Maojun},
        TITLE = {ThermalGS: Dynamic 3D Thermal Reconstruction with Gaussian Splatting},
        JOURNAL = {Remote Sensing},
        VOLUME = {17},
        YEAR = {2025},
        NUMBER = {2},
        ARTICLE-NUMBER = {335},
        URL = {https://www.mdpi.com/2072-4292/17/2/335},
        ISSN = {2072-4292},
        DOI = {10.3390/rs17020335}
        }
      
      links:
          - name: Paper
            url: "https://www.mdpi.com/2072-4292/17/2/335"
        
          - name: Code
            url: "https://github.com/porcofly/ThermalGS-and-TSDN-Dataset"


---

Our lab pioneers **3D geospatial intelligence** with a focus on:

**‌●‌**   Planet-Scale Digital Twins – Generating accurate, photorealistic, semantic, and real-time 3D reconstructions of Earth’s surface for intelligently path planning, equipment and target geolocation, and geospatial analysis.

**‌●‌**   GPS-Independent UAV Localization – Enabling drones to geolocate and navigate using various map representations (e.g., textured model, white model, DOM+DSM and DOM+DEM) in GPS-denied environments.

**‌●‌**   Physics-Based Multimodal Simulation – Developing immersive virtual environments for UAV perception, planning, and localization training via sensor simulation (RGB, thermal, LiDAR, et.al).

![](img/research/r3.png)
