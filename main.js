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

  // --- LISTING CARD NAVIGATION ---
  const listingIdMap = {
  "american legion": "american-legion",
  "disabled american veterans (dav)": "disabled-american-veterans",
  "veterans of foreign wars (vfw)": "vfw",
  "military officers association of america (moaa)": "moaa",
  "paralyzed veterans of america (pva)": "paralyzed-veterans",
  "amvets": "amvets",
  "vietnam veterans of america (vva)": "vietnam-veterans-america",
  "iraq and afghanistan veterans of america (iava)": "iava",
  "student veterans of america (sva)": "student-veterans-america",
  "gold star wives of america": "gold-star-wives",
  "swords to plowshares": "swords-to-plowshares",
  "veterans consortium pro bono program": "veterans-consortium-pro-bono",
  "national veterans legal services program (nvlsp)": "national-veterans-legal-services",
  "chisholm chisholm & kilpatrick (cck law)": "chisholm-chisholm-kilpatrick",
  "berry law firm": "berry-law-firm",
  "attig steel pllc": "attig-steel",
  "marc whitehead & associates": "marc-whitehead-associates",
  "perkins studdard llc": "perkins-studdard",
  "woods & woods": "woods-and-woods",
  "hill & ponton": "hill-and-ponton",
  "veterans law group": "veterans-law-group",
  "cavc pro se practice": "cavc-pro-se-practice",
  "jan dils attorneys at law": "jan-dils-attorneys",
  "telemedica": "telemedica",
  "nexus letters (nexusletters.com)": "nexus-letters-finnerty",
  "combat craig": "combat-craig",
  "fisher house foundation": "fisher-house",
  "gary sinise foundation": "gary-sinise-foundation",
  "team red white & blue (team rwb)": "team-red-white-blue",
  "wounded warrior project (benefits services)": "wounded-warrior-project",
  "national veterans foundation": "national-veterans-foundation",
  "travis manion foundation": "travis-manion-foundation",
  "the independence fund": "independence-fund",
  "united states veterans initiative (u.s.vets)": "us-vets",
  "psycharmor": "psycharmor",
  "operation first response": "operation-first-response",
  "vethelp (vethelp.us)": "vethelp",
  "vfw foundation": "vfw-foundation",
  "pat tillman foundation": "pat-tillman-foundation",
  "county veterans service officers (cvsos)": "county-veterans-service-officers",
  "va pact act resources": "va-pact-act",
  "camp lejeune claims (va)": "va-camp-lejeune",
  "american red cross (military families)": "american-red-cross-military"
  };
  document.querySelectorAll('.listing-card').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
      // Don't intercept clicks on the "Visit Website" button
      if (e.target.closest('.btn-visit')) return;
      const name = (card.dataset.name || '').toLowerCase();
      const id = listingIdMap[name];
      if (id) window.location.href = 'listings/' + id + '.html';
    });
  });
});
