# # Updating the code to handle UTF-8 characters using an alternative library if necessary.
# from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         # Title
#         self.set_font("Arial", "B", 16)
#         self.cell(0, 10, "Bourama Ngom - Développeur Full Stack Junior", ln=True, align="C")
#         self.set_font("Arial", "", 12)
#         self.cell(0, 10, "Téléphone : +221 78 371 84 72 | Email : ngombourama@gmail.com", ln=True, align="C")
#         self.cell(0, 10, "Dakar, Sénégal", ln=True, align="C")
#         self.ln(10)

# # Create instance of PDF class
# pdf = PDF()
# pdf.add_page()

# # Add sections
# sections = {
#     "Profil": """Développeur Full Stack autodidacte, passionné par la création d'applications web robustes et performantes. Doté d’une solide polyvalence technique, capable de naviguer aisément entre différents langages de programmation et frameworks. Toujours prêt à relever de nouveaux défis et acquérir de nouvelles compétences.""",

#     "Expérience Professionnelle": """Développeur Full Stack & DevOps
#     WAW-Telecom, Dakar, Sénégal | Stage | 2023 – Présent
#     - Création de modules Odoo pour automatiser et améliorer le CRM.
#     - Développement et maintenance du site web wawtelecom.com.
#     - Intégration API entre le site web et Odoo, facilitant la gestion de leads.

#     Développeur Laravel
#     Plateforme E-Commerce - marchecolobane.com | 2022 – 2023
#     - Analyse des besoins techniques et développement de la plateforme en Laravel 10.
#     - Déploiement et intégration continue (CI/CD) avec GitHub et GitLab CI.
#     - Sécurisation des communications backend-frontend pour répondre aux normes de sécurité.

#     Développeur Web & Mobile Laravel
#     Projet WeerGu-Yaram | 2022 – 2023
#     - Développement d'une plateforme en Laravel avec intégration React pour le frontend.
#     - Analyse des besoins, modélisation de données et gestion de la liaison backend-frontend.

#     Développeur Web Symfony
#     Projet Mlouma.com | 2021 – 2022
#     - Maintenance et correctifs, ainsi que refonte de sites web pour une plateforme agricole.
#     - Mise en place de l’authentification à deux facteurs.""",

#     "Compétences": """Développement : Laravel, Symfony, Angular, React, Odoo
#     Gestion de projets : Méthodologies agiles (Scrum)
#     Développement d’API : Conception et sécurisation d’API RESTful, Authentification JWT
#     Déploiement et Conteneurisation : Docker, CI/CD avec GitHub et GitLab CI
#     Sécurité Informatique : Tests unitaires, tests de pénétration, analyse de sécurité
#     Outils et Frameworks : Docker, Git, Swagger""",

#     "Formation": """Certification Développeur Backend - Simplon Sénégal, Dakar (2023)
#     Certification Développeur Web & Mobile - ESP, Dakar (2022)
#     Certifié Security Analyste - IBM (2022)
#     ISO/IEC-270001 - ESP & Skillfront (2022)
#     DUT Génie Informatique - ESP, Dakar (2021)
#     Google IT Support - Google (2021)""",

#     "Centres d’intérêt": """Veille technologique, lecture, jeux vidéo, mangas"""
# }

# for section, content in sections.items():
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, section, ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.multi_cell(0, 10, content)
#     pdf.ln(5)

# # Save the PDF
# output_path = "/mnt/data/Bourama_Ngom_CV_Canada.pdf"
# pdf.output(output_path)

# output_path











from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

output_path = "Bourama_Ngom_CV_Canada.pdf"
pdf = canvas.Canvas(output_path, pagesize=A4)
pdf.setFont("Helvetica", 12)

# Coordonnées de base pour positionner le texte
x, y = 50, 800

# Titre et contact
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(x, y, "Bourama Ngom - Développeur Full Stack Junior")
y -= 20
pdf.setFont("Helvetica", 12)
pdf.drawString(x, y, "Téléphone : +221 78 371 84 72 | Email : ngombourama@gmail.com")
y -= 15
pdf.drawString(x, y, "Dakar, Sénégal")
y -= 30

# Contenu des sections
# Add sections
sections = {
    "Profile": """Self-taught Full Stack Developer, passionate about creating robust and high-performing web applications. Skilled in various programming languages and frameworks, adaptable to new challenges, and quick to learn in any technical area.""",

    "Professional Experience": """Full Stack Developer & DevOps
    WAW-Telecom, Dakar, Senegal | Internship | 2023 – Present
    - Created Odoo modules to automate and improve CRM processes.
    - Developed and maintained the wawtelecom.com website.
    - Integrated API between the website and Odoo to streamline lead management.

    Laravel Developer
    E-Commerce Platform - marchecolobane.com | 2022 – 2023
    - Analyzed technical requirements and developed the platform using Laravel 10.
    - Implemented continuous integration (CI/CD) with GitHub and GitLab CI.
    - Secured backend-frontend communications according to security standards.

    Web & Mobile Developer with Laravel
    Project WeerGu-Yaram | 2022 – 2023
    - Developed a platform using Laravel with frontend integration in React.
    - Analyzed requirements, modeled data, and managed backend-frontend linkage.

    Symfony Web Developer
    Project Mlouma.com | 2021 – 2022
    - Maintained and improved the website for an agricultural platform.
    - Implemented two-factor authentication.""",

    "Skills": """Development: Laravel, Symfony, Angular, React, Odoo
    Project Management: Agile methodologies (Scrum)
    API Development: Designing and securing RESTful APIs, JWT Authentication
    Deployment and Containerization: Docker, CI/CD with GitHub and GitLab CI
    IT Security: Unit tests, penetration testing, security analysis
    Tools & Frameworks: Docker, Git, Swagger""",

    "Education": """Backend Developer Certification - Simplon Senegal, Dakar (2023)
    Web & Mobile Developer Certification - ESP, Dakar (2022)
    Security Analyst Certification - IBM (2022)
    ISO/IEC-270001 - ESP & Skillfront (2022)
    DUT in Computer Engineering - ESP, Dakar (2021)
    Google IT Support Specialization - Google (2021)""",

    "Interests": """Technology watch, reading, video games, anime"""
}

# Insère chaque section dans le PDF
for section, content in sections.items():
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, section)
    y -= 20
    pdf.setFont("Helvetica", 12)
    for line in content.splitlines():
        pdf.drawString(x, y, line)
        y -= 15
    y -= 10  # Espace entre sections

pdf.save()
print(f"PDF généré avec succès : {output_path}")
