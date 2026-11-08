---
# An instance of the Portfolio widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: project

active: false

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 50

title: 科研项目
subtitle: Selected research projects and papers.

project_list:

  - title: "TNNLS 2021: Cascaded Correlation Refinement for Robust Deep Tracking"
    desc: |
      In this paper, we propose a cascaded correlation refinement approach to facilitate the robustness of deep tracking. Our approach cascades multiple stages of correlation refinement to progressively refine target localization. We introduce an explicit measure to identify the tracking failure and then leverage a simple yet effective look-back scheme to adaptively incorporate the initial model and on-the-fly model to update the tracking model.
    image: /img/projects/ccr.png
    time: 
    links:
      - name: Project
        url: https://github.com/983632847/CCR
      - name: Paper
        url: https://ieeexplore.ieee.org/document/9069312
      - name: Code
        url: https://github.com/983632847/CCR    
      


  - title: "ACM MM 2020: Accurate UAV Tracking with Distance-Injected Overlap Maximization"
    desc: |
      In this work, we propose distance-injected overlap maximization for accurate UAV tracking. We use distance-injected semantic IoU loss to alleviate the drift problem caused by dual-dynamic disturbances. Furthermore, we conduct feature recalibration network and multi-scale feature concat that improve adaptive feature extraction for UAV targets.
    image: /img/projects/utrack.png
    time: 
    links:
      - name: Conference
        url: https://2020.acmmm.org/
      - name: Project
        url: https://dl.acm.org/doi/10.1145/3394171.3413959
      - name: Paper
        url: https://dl.acm.org/doi/10.1145/3394171.3413959
      - name: Code
        url: https://dl.acm.org/doi/10.1145/3394171.3413959    
      







---


