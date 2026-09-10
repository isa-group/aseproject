---
# Leave the homepage title empty to use the site title
title: ''
# date: 2022-10-24
show_date: false
type: landing

sections:
  - block: ase-hero
    id: hero
    content:
      eyebrow: Human-centred software engineering and AI
      title: Augmented Software Engineering
      suffix: ASE
      facts:
        - 2025–2028
        - Universidad de Sevilla
        - PID2024-156482NB-I00
      cta:
        label: Explore the vision
        url: '#about'
      cta_alt:
        label: View publications
        url: '#publications'
      social:
        - icon: github
          label: GitHub
          url: https://github.com/isa-group/aseproject
        - icon: linkedin
          label: LinkedIn
          url: https://www.linkedin.com/feed/hashtag/aseproject/
  - block: markdown
    id: about
    content:
      title: Vision
      subtitle: Human-centred by design
      text: |-
        <div class="ase-vision-copy">
        Aligned with current initiatives shaping the roadmap of SE over the next decade, the ASE project presents the notion of Augmented Software Engineering (ASE), emphasising how technologies will progressively enhance the capabilities of software engineers, while keeping them in control, enabling the development of more sophisticated and reliable software solutions. Accordingly, the goal of ASE is to augment the capabilities of software engineers in requirements, testing, and their intersection by designing human-centred tools, techniques, and processes. To achieve this objective, we will focus on three key differentiating points: 1) the interconnection between requirements and software testing as a fundamental enabler for validating AI-generated software applications, 2) a holistic approach that integrates tools, processes, and people, with the needs of engineers serving as the cornerstone for all decision-making, and 3) the adoption of disruptive technologies, including but not limited to GenAI, to support engineers throughout the software development lifecycle.
        </div>

        <div class="ase-pillars">
          <div><span>01</span><strong>Requirements and testing connected</strong></div>
          <div><span>02</span><strong>Tools, processes and people integrated</strong></div>
          <div><span>03</span><strong>Engineers remain firmly in control</strong></div>
        </div>
    design:
      columns: '2'
  - block: collection
    id: members
    content:
      title: Our Team
      filters:
        folders:
          - members
    design:
      columns: '2' 
      view: compact #mansory 
      flip_alt_rows: false
  - block: collection
    id: publications
    content:
      title: Publications 
      filters:
        folders:
         - publications
        featured_only: true
    design:
      columns: '2'
      view: compact #Citation # card
  - block: collection
    id: events
    content:
      title: Events
      filters:
        folders:
          - events
    design:
      columns: '2'
      view: compact
  - block: collection
    id: videos
    content:
      title: Videos
      show_date: false
      filters:
        folders:
          - event
    design:
      columns: '2'
      view: compact
      show_date: false
  - block: collection
    id: datasets
    content:
      title: Datasets
      show_date: false
      filters:
        folders:
          - datasets  
    design:
      columns: '2'
      view: compact
  - block: collection
    id: collaborators
    content:
      title: Collaborators
      filters:
        folders:
          - collaborators
    design:
      columns: '2'
      view: compact     
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      # Contact (add or remove contact options as necessary)
      email: sergiosegura [AT] us [DOT] es #test@example.org
      # phone: 888 888 88 88
      # appointment_url: 'https://calendly.com'
      address:
        street: Avda. Reina Mercedes
        city: Seville
        region: Seville
        postcode: '41012'
        country: España
        country_code: ES
      directions: Universidad de Sevilla

      # Choose a map provider in `params.yaml` to show a map from these coordinates
      coordinates:
        latitude: '37.3583821'
        longitude: '-5.9876975'  
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
    design:
      columns: '2'
      view: compact
---
