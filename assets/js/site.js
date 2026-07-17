document.documentElement.classList.remove("no-js");

const header = document.querySelector("[data-header]");
const menuButton = document.querySelector("[data-menu-toggle]");
const menu = document.querySelector("[data-menu]");

const closeMenu = () => {
  if (!menuButton || !menu) return;
  menuButton.setAttribute("aria-expanded", "false");
  menu.classList.remove("is-open");
  document.body.classList.remove("menu-open");
};

if (menuButton && menu) {
  menuButton.addEventListener("click", () => {
    const isOpen = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!isOpen));
    menu.classList.toggle("is-open", !isOpen);
    document.body.classList.toggle("menu-open", !isOpen);
  });

  menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 900) closeMenu();
  });
}

const scrollTopButton = document.querySelector("[data-scroll-top]");
const HIDE_AFTER = 260;
let lastY = window.scrollY;

const updateHeader = () => {
  const y = Math.max(0, window.scrollY);
  header?.classList.toggle("is-scrolled", y > 12);
  if (header && Math.abs(y - lastY) > 4) {
    const hide =
      y > lastY &&
      y > HIDE_AFTER &&
      !document.body.classList.contains("menu-open") &&
      !header.contains(document.activeElement);
    header.classList.toggle("is-hidden", hide);
    lastY = y;
  }
  scrollTopButton?.classList.toggle("is-visible", y > 600);
};
updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

window.addEventListener(
  "pointermove",
  (event) => {
    if (event.pointerType !== "mouse" || event.clientY > 90) return;
    header?.classList.remove("is-hidden");
  },
  { passive: true },
);

header?.addEventListener("focusin", () => header.classList.remove("is-hidden"));

scrollTopButton?.addEventListener("click", () => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
});

const revealElements = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -5%" },
  );
  revealElements.forEach((element) => revealObserver.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add("is-visible"));
}

document.querySelectorAll("[data-room-control]").forEach((control) => {
  const output = control.querySelector("[data-state]");
  const activeClass = control.classList.contains("is-secure") ? "is-secure" : "is-on";
  if (output) output.dataset.value = output.textContent;
  control.addEventListener("click", () => {
    const active = control.getAttribute("aria-pressed") === "true";
    control.setAttribute("aria-pressed", String(!active));
    control.classList.toggle(activeClass, !active);
    if (output) output.textContent = active ? "—" : output.dataset.value;
  });
});

const sceneToggle = document.querySelector("[data-scene-toggle]");
if (sceneToggle) {
  sceneToggle.addEventListener("click", () => {
    const active = sceneToggle.getAttribute("aria-pressed") === "true";
    sceneToggle.setAttribute("aria-pressed", String(!active));
    sceneToggle.classList.toggle("is-on", !active);
  });
}

document.querySelectorAll(".faq-list details").forEach((detail) => {
  detail.addEventListener("toggle", () => {
    if (!detail.open) return;
    document.querySelectorAll(".faq-list details[open]").forEach((openDetail) => {
      if (openDetail !== detail) openDetail.removeAttribute("open");
    });
  });
});
