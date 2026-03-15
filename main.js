// VA Claims Help Finder — Main JS

// --- NAV: Hamburger & Dropdown ---
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
  }

  const dropdown = document.querySelector('.dropdown');
  if (dropdown) {
    dropdown.addEventListener('click', (e) => {
      e.stopPropagation();
      dropdown.classList.toggle('open');
    });
    document.addEventListener('click', () => dropdown.classList.remove('open'));
  }

  // --- SEARCH FILTER ---
  const searchInput = document.getElementById('search');
  if (searchInput) {
    searchInput.addEventListener('keyup', () => {
      const q = searchInput.value.toLowerCase().trim();
      document.querySelectorAll('.listing-card').forEach(card => {
        const name = (card.dataset.name || '').toLowerCase();
        const type = (card.dataset.type || '').toLowerCase();
        card.classList.toggle('hidden', q && !name.includes(q) && !type.includes(q));
      });
    });
  }

  // --- SMOOTH SCROLL ---
  document.querySelectorAll('a[href="#listings"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.getElementById('listings');
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });

  // --- INTERSECTION OBSERVER: animate cards ---
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const card = entry.target;
        const idx = parseInt(card.dataset.idx || 0);
        setTimeout(() => card.classList.add('visible'), idx * 80);
        observer.unobserve(card);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.listing-card, .category-card').forEach((card, i) => {
    card.dataset.idx = i;
    observer.observe(card);
  });

  // --- SUBMIT FORM ---
  const form = document.getElementById('submit-form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const required = form.querySelectorAll('[required]');
      let valid = true;
      required.forEach(f => { if (!f.value.trim()) { f.style.borderColor = 'var(--red)'; valid = false; } else { f.style.borderColor = '#ddd'; } });
      if (valid) {
        form.style.display = 'none';
        document.getElementById('form-success').style.display = 'block';
      }
    });
  }
});
