// Smooth scrolling functionality
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start' 
        });
    }
}

// Contact form handling
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            handleFormSubmission(this);
        });
    }
});

function handleFormSubmission(form) {
    // Get form data
    const formData = new FormData(form);
    const data = {};
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    // Create email subject and body
    const subject = data.userType === 'contractor' 
        ? `New Contractor Inquiry from ${data.name}`
        : `New Job Seeker Application from ${data.name}`;
    
    const body = `
Name: ${data.name}
Email: ${data.email}
Type: ${data.userType}
Company: ${data.company || 'N/A'}

Message:
${data.message}

---
Sent from Lemmik Construction Recruiting website
    `.trim();
    
    // Create mailto link
    const mailtoLink = `mailto:charles.lemmik@proton.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    
    // Show success message
    showMessage('Thank you! Opening your email client...', 'success');
    
    // Open email client
    window.location.href = mailtoLink;
    
    // Reset form after short delay
    setTimeout(() => {
        form.reset();
    }, 1000);
}

function showContactForm(userType) {
    // Scroll to contact section
    scrollToSection('contact');
    
    // Set the user type in the form
    setTimeout(() => {
        const userTypeSelect = document.querySelector('select[name="userType"]');
        if (userTypeSelect) {
            userTypeSelect.value = userType;
        }
    }, 800);
}

function showMessage(message, type = 'info') {
    // Create message element
    const messageEl = document.createElement('div');
    messageEl.className = `message message-${type}`;
    messageEl.innerHTML = message;
    
    // Style the message
    Object.assign(messageEl.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        background: type === 'success' ? '#27ae60' : '#3498db',
        color: 'white',
        padding: '1rem 2rem',
        borderRadius: '5px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
        zIndex: '10000',
        animation: 'slideIn 0.3s ease'
    });
    
    // Add animation styles if not exists
    if (!document.querySelector('#message-styles')) {
        const styles = document.createElement('style');
        styles.id = 'message-styles';
        styles.innerHTML = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
        `;
        document.head.appendChild(styles);
    }
    
    // Add to page
    document.body.appendChild(messageEl);
    
    // Remove after 4 seconds
    setTimeout(() => {
        messageEl.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (messageEl.parentNode) {
                messageEl.parentNode.removeChild(messageEl);
            }
        }, 300);
    }, 4000);
}

// Add scroll effects for navigation
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.3)';
    } else {
        navbar.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
    }
});

// Add click handlers for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            scrollToSection(targetId);
        });
    });
});