import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Ashish M Y - Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1.5rem;
    }
    .skill-tag {
        display: inline-block;
        background: #e9ecef;
        color: #495057;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        margin: 0.25rem 0.25rem 0 0;
        font-size: 0.875rem;
    }
    .contact-info {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: #f1f3f4;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .stat-item {
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎨 Portfolio Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "📊 About & Skills", "🎯 Featured Projects", "📞 Contact"]
)

# Helper function to create skill tags
def create_skill_tags(skills):
    html = ""
    for skill in skills:
        html += f'<span class="skill-tag">{skill}</span>'
    return html

# HOME PAGE
if page == "🏠 Home":
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🎨 Ashish M Y</h1>
        <h2>Content Creator & Visual Storyteller</h2>
        <p>Creating content that doesn't just inform—it inspires and connects</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Projects Completed", "10+", "+3 this month")
    with col2:
        st.metric("Team Collaborations", "20+", "Faculty & Students")
    with col3:
        st.metric("Design Tools", "5", "Mastered")
    with col4:
        st.metric("Publications", "3", "Magazine Issues")
    
    st.markdown("---")
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("👋 Welcome to My Creative World")
        st.write("""
        I'm a creative storyteller who bridges the gap between compelling narratives and visual design. 
        With hands-on experience creating everything from institutional magazines to personal brand campaigns, 
        I specialize in content that serves both business goals and human connection.
        
        **Currently:** B.Tech-IT 2nd Year, Alliance School of Advanced Computing  
        **Focus:** Building my startup while leading editorial and design projects  
        **Passion:** Creating content that makes people stop, think, and feel
        """)
        
        st.subheader("🚀 What Makes Me Different")
        st.write("""
        - **Strategic + Creative:** I don't just make things look good—I make them work
        - **Full-Stack Content:** Writing, design, video, and strategy in one person
        - **Leadership Experience:** Managing teams and delivering results under pressure
        - **Startup Mindset:** Understanding business goals and user needs
        """)
    
    with col2:
        st.subheader("🎯 Quick Overview")
        st.info("""
        **Location:** Bengaluru, Karnataka  
        **Experience:** 2+ years  
        **Specialties:**
        - Editorial Design
        - Content Strategy  
        - Visual Storytelling
        - Team Leadership
        """)
        
        st.success("**Available for:**\n- Full-time positions\n- Internships\n- Freelance projects")

# ABOUT & SKILLS PAGE
elif page == "📊 About & Skills":
    st.title("📊 About Me & Skills")
    
    # About Me Section
    st.subheader("🎯 My Story")
    st.write("""
    I started as a curious student who loved both writing and design. What began with creating posters 
    for college events has evolved into leading editorial teams, managing university publications, and 
    building my own startup. I've learned that the best content happens at the intersection of 
    strategy, creativity, and genuine human connection.
    
    Today, I'm equally comfortable writing compelling narratives, designing magazine layouts, 
    editing videos, or presenting to stakeholder groups. My goal is simple: create content 
    that doesn't just fill space—it fills a need.
    """)
    
    # Skills Section
    st.subheader("🛠️ Core Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Content Strategy & Writing**")
        writing_skills = ["Editorial Writing", "Brand Storytelling", "Social Media Content", 
                         "Blog Management", "Copywriting", "Research & Interviews"]
        st.markdown(create_skill_tags(writing_skills), unsafe_allow_html=True)
        
        st.markdown("**Digital Content Creation**")
        digital_skills = ["Video Editing", "WordPress", "Presentation Design", 
                         "Content Calendar", "SEO Basics", "Analytics"]
        st.markdown(create_skill_tags(digital_skills), unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Visual Design & Production**")
        design_skills = ["Magazine Layout", "Poster Design", "Brand Identity", 
                        "Photo Editing", "Print Production", "UI/UX Basics"]
        st.markdown(create_skill_tags(design_skills), unsafe_allow_html=True)
        
        st.markdown("**Leadership & Collaboration**")
        leadership_skills = ["Team Management", "Project Coordination", "Public Speaking", 
                           "Client Relations", "Deadline Management", "Cross-functional Teams"]
        st.markdown(create_skill_tags(leadership_skills), unsafe_allow_html=True)
    
    # Tools & Software
    st.subheader("⚡ Tools & Software")
    
    tool_col1, tool_col2, tool_col3 = st.columns(3)
    
    with tool_col1:
        st.markdown("**Design**")
        st.markdown("• Canva (Advanced)")
        st.markdown("• Adobe Photoshop")
        st.markdown("• Figma (Basic)")
        
    with tool_col2:
        st.markdown("**Content & Web**")
        st.markdown("• WordPress")
        st.markdown("• Google Workspace")
        st.markdown("• Microsoft Office")
        
    with tool_col3:
        st.markdown("**Other**")
        st.markdown("• Video Editing Software")
        st.markdown("• Social Media Platforms")
        st.markdown("• Project Management Tools")

# FEATURED PROJECTS PAGE
elif page == "🎯 Featured Projects":
    st.title("🎯 Featured Projects & Portfolio")
    
    # Note about images
    st.info("📸 **Note:** Upload your project images to the same folder as this app for full visual portfolio display")
    
    # Project 1: MAGIC Campaign
    st.markdown("""
    <div class="project-card">
        <h3>🌟 "MAGIC - Moments and Memories" Campaign</h3>
        <p><strong>Role:</strong> Creative Director, Designer</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Try to load image, show placeholder if not found
        try:
            magic_image = Image.open("magic_poster.jpg")  # You'll upload this
            st.image(magic_image, caption="MAGIC Campaign Poster")
        except:
            st.image("https://via.placeholder.com/400x600/667eea/ffffff?text=MAGIC+Poster", 
                    caption="MAGIC Campaign Poster (Upload magic_poster.jpg)")
    
    with col2:
        st.write("""
        **Project Overview:**
        - Conceptualized nature-themed promotional campaign with "Magic begins 5 Aug" messaging
        - Designed elegant poster featuring dreamy forest photography with butterfly motifs
        - Created sophisticated typography hierarchy balancing branding with tagline
        - Developed cohesive visual identity for multi-touchpoint campaign
        
        **Skills Demonstrated:**
        • Creative Conceptualization • Visual Hierarchy • Nature Photography Integration • Brand Development
        """)
    
    st.markdown("---")
    
    # Project 2: Alliance University Publications
    st.markdown("""
    <div class="project-card">
        <h3>📚 Alliance University Publications Suite</h3>
        <p><strong>Role:</strong> Editor, Designer, Content Creator</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Subproject 2a: Green Chronicle
    st.subheader("📗 Green Chronicle Magazine (March 2025)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            chronicle_image = Image.open("green_chronicle.jpg")
            st.image(chronicle_image, caption="Green Chronicle Cover")
        except:
            st.image("https://via.placeholder.com/400x500/28a745/ffffff?text=Green+Chronicle", 
                    caption="Green Chronicle Cover (Upload green_chronicle.jpg)")
    
    with col2:
        st.write("""
        **Project Details:**
        - Lead designer for Alliance NE 3.0 festival publication featuring "Innovation | Culture | Athleticism"
        - Created comprehensive magazine layout incorporating UN SDG wheel and diverse content sections
        - Maintained brand consistency across Alliance University and NAAC Grade A+ accreditation messaging
        - Designed engaging cover balancing institutional credibility with youthful energy
        """)
    
    # Subproject 2b: Subscription Brochure
    st.subheader("📄 Subscription Brochure Design")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            brochure_image = Image.open("alliance_brochure.jpg")
            st.image(brochure_image, caption="Alliance Subscription Brochure")
        except:
            st.image("https://via.placeholder.com/400x500/17a2b8/ffffff?text=Alliance+Brochure", 
                    caption="Subscription Brochure (Upload alliance_brochure.jpg)")
    
    with col2:
        st.write("""
        **Features:**
        - Developed promotional brochure with QR code integration for digital engagement
        - Created clean, modern layout featuring university architecture photography
        - Implemented "Bigger, Bolder, Better" messaging strategy with clear call-to-action design
        - Coordinated with 20+ team members across faculty and students
        """)
    
    st.markdown("---")
    
    # Project 3: Editorial Writing
    st.markdown("""
    <div class="project-card">
        <h3>✍️ "She Carries the Village, She Faces the City" Feature</h3>
        <p><strong>Role:</strong> Writer, Visual Curator</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            article_image = Image.open("village_city_article.jpg")
            st.image(article_image, caption="Feature Article Layout")
        except:
            st.image("https://via.placeholder.com/400x500/6f42c1/ffffff?text=Article+Layout", 
                    caption="Article Layout (Upload village_city_article.jpg)")
    
    with col2:
        st.write("""
        **Editorial Excellence:**
        - Authored compelling narrative exploring women's educational journeys from rural to urban settings
        - Developed "Empowered by Education: A Girl's Journey from Village to City" campaign messaging
        - Integrated atmospheric photography with moody landscapes that enhance storytelling
        - Created engaging layout design with "IT'S ALL ABOUT HER" visual theme
        - Wrote inspirational conclusion resonating with universal themes of education and courage
        
        **Impact:** Content that resonates beyond academic audiences, inspiring readers across demographics
        """)
    
    # Additional Projects Summary
    st.subheader("🚀 Additional Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Freelance Digital Projects**
        - WordPress blog setup and design for clients
        - Custom birthday magazines with personal photography
        - Video content production for events
        - Social media strategy development
        """)
    
    with col2:
        st.markdown("""
        **Startup MVP Development** *(Ongoing)*
        - Leading all content strategy for startup launch
        - Creating investor pitch decks and presentations
        - Developing brand voice across touchpoints
        - Managing content calendar and marketing materials
        """)

# CONTACT PAGE
elif page == "📞 Contact":
    st.title("📞 Let's Create Something Amazing Together")
    
    # Contact Header
    st.markdown("""
    <div class="main-header">
        <h2>Ready to Collaborate?</h2>
        <p>I'm excited to discuss how my creative vision and technical skills can contribute to your team</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Information
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📧 Contact Information")
        
        st.markdown("""
        <div class="contact-info">
            <strong>📧 Email:</strong> [your.email@gmail.com]<br>
            <strong>📱 Phone:</strong> [+91-XXXXX-XXXXX]<br>
            <strong>📍 Location:</strong> Bengaluru, Karnataka<br>
            <strong>🎓 Institution:</strong> Alliance School of Advanced Computing<br>
            <strong>💼 LinkedIn:</strong> [linkedin.com/in/yourprofile]<br>
            <strong>🌐 Portfolio:</strong> [your-portfolio-site.com]
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("⏰ Availability")
        st.success("""
        **Current Status:** Open for opportunities  
        **Available for:**
        - Full-time positions
        - Internships (3-6 months)
        - Freelance projects
        - Consultation calls
        
        **Preferred Start:** Immediate
        """)
    
    with col2:
        st.subheader("💬 Send Me a Message")
        
        # Contact form (will work when hosted)
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            company = st.text_input("Company/Organization (Optional)")
            message_type = st.selectbox(
                "I'm interested in:",
                ["Content Creator Position", "Freelance Project", "Internship Opportunity", 
                 "Collaboration", "General Inquiry"]
            )
            message = st.text_area("Your Message", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀")
            
            if submitted:
                st.success(f"Thanks {name}! I'll get back to you soon. For immediate response, please email me directly.")
    
    # Call to Action
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 For Hiring Managers**
        Ready to see how I can contribute to your content team? Let's schedule a portfolio walkthrough where I can show you each project in detail.
        """)
    
    with col2:
        st.markdown("""
        **🤝 For Collaborators**
        Have a creative project in mind? Whether it's content strategy, design, or full campaign development, I'm excited to explore partnerships.
        """)
    
    with col3:
        st.markdown("""
        **🚀 For Startups**
        Need someone who understands the startup hustle? I bring both creative skills and entrepreneurial mindset to early-stage companies.
        """)
    
    # Final CTA
    st.markdown("""
    <div class="main-header">
        <h3>Let's Turn Ideas Into Impact</h3>
        <p>Every great project starts with a conversation. Reach out and let's discuss your content needs!</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; padding: 1rem;">
    <p>✨ Built with Streamlit • Designed by Ashish M Y • 2025 ✨</p>
    <p><em>"Creating content that doesn't just inform—it inspires and connects"</em></p>
</div>
""", unsafe_allow_html=True)
