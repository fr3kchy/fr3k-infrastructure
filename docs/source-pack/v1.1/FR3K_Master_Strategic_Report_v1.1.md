# FR3K: Master Strategic Implementation Plan

**Free Communications. Open Infrastructure. AI Driven. Community Built.**

**Version:** 1.1  
**Date:** August 2026  
**Status:** Implementation Baseline

---

## 1. Executive Summary

FR3K is an engineering-led initiative focused on building resilient, community-owned communications infrastructure in North Queensland. The project prioritizes **transparent experimentation**, **reproducible evidence**, and **regulatory compliance**. 

The core strategic thesis is that by documenting both successes and failures in a difficult tropical environment, FR3K builds the trust necessary to attract contributors, partners, and sustainable funding.

---

## 2. Strategic Risk & Mitigation

To ensure the long-term viability and safety of the project, the following primary risks have been identified along with their corresponding mitigation strategies.

| Risk Category | Primary Threat | Mitigation Strategy | Accountable |
| :--- | :--- | :--- | :--- |
| **Regulatory** | ACMA non-compliance or interference complaint. | Mandatory RF Lead sign-off for every unique radio/antenna configuration; documented EIRP/PSD calculations. | RF Lead |
| **Legal** | Unauthorised site access or liability from equipment failure. | Written site permissions (SOP-06); clear "supplementary infrastructure" disclaimers; robust insurance coverage. | Operations Lead |
| **Technical** | Hardware failure due to tropical corrosion or thermal stress. | Marine-grade enclosures; thermal testing under peak load; conservative solar yield modeling (SOP-08). | Engineering Lead |
| **Safety** | Team injury during field deployment or battery incident. | Mandatory safety briefings; "Stop Work" authority for all members; LiFePO4 chemistry for unattended nodes. | Safety Lead |
| **Community** | Misinformation or loss of trust due to unsupported claims. | "Evidence-first" publishing; mandatory human review of all AI content; transparent failure reporting. | Program Lead |

---

## 3. Technical Architecture & Regulatory Guardrails

### 3.1 Layered Network Design
FR3K employs a layered architecture to ensure flexibility and resilience:
- **Meshtastic:** Accessible, handheld LoRa ecosystem for field teams and introductory workshops.
- **Reticulum/LXMF:** The principal research architecture for identity, resilient messaging, and multi-interface routing.
- **Backhaul:** Agnostic support for Ethernet, Wi-Fi, and satellite (e.g., Starlink) where appropriate.

### 3.2 ACMA Compliance Checklist
All FR3K transmissions must adhere to the **Radiocommunications (Low Interference Potential Devices) Class Licence 2025**.

| Requirement | Verification Step | Status |
| :--- | :--- | :--- |
| **Frequency** | Confirmed within 915–928 MHz band. | [ ] |
| **Modulation** | Digital modulation or frequency hopping verified. | [ ] |
| **Power** | Conducted power and antenna gain result in compliant EIRP. | [ ] |
| **PSD** | Peak Power Spectral Density within 8 dBm/3 kHz (if applicable). | [ ] |
| **Hardware** | Equipment carries required compliance markings. | [ ] |
| **Sign-off** | RF Lead has reviewed and signed the compliance record. | [ ] |

---

## 4. 90-Day Launch Roadmap

The first 90 days focus on establishing a credible technical and operational baseline.

1.  **Phase 1: Bench & Baseline (Days 1-30)**
    *   Finalize P0 Bench Reference design.
    *   Complete initial ACMA compliance audit for all core hardware.
    *   Establish documentation and media pipelines.
2.  **Phase 2: Controlled Pilots (Days 31-60)**
    *   Deploy first P1 Portable Field Kits for range surveys.
    *   Secure first two private host sites for P2 nodes.
    *   Launch the "Scout" volunteer onboarding pathway.
3.  **Phase 3: Community Exercise (Days 61-90)**
    *   Conduct first governed community messaging exercise.
    *   Publish "Month 2" KPI and evidence report.
    *   Review and refine architecture for regional expansion.

---

## 5. AI & Hermes Governance

AI is used as an **amplifier**, not a replacement for human judgment.
- **Traceability:** Every AI-generated asset must link to its prompt, model, and human reviewer.
- **Honesty:** Conceptual imagery must be clearly labeled to avoid confusion with real deployment evidence.
- **Safety:** AI is never permitted in safety-critical control loops.

---

## 6. Conclusion

FR3K is not just a network of nodes; it is a network of people. By maintaining a disciplined, evidence-based approach, we provide a blueprint for regional resilience that can be reproduced by communities across Australia and beyond.
