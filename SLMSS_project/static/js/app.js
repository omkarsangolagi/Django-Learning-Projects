document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  if (toggle && nav) toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? '×' : '☰';
  });

  document.querySelectorAll('.password-toggle').forEach(button => button.addEventListener('click', () => {
    const input = button.closest('.password-wrap').querySelector('input');
    const visible = input.type === 'text';
    input.type = visible ? 'password' : 'text';
    button.textContent = visible ? 'Show' : 'Hide';
  }));

  const leaveForm = document.querySelector('[data-leave-form]');
  if (leaveForm) leaveForm.addEventListener('submit', event => {
    const start = leaveForm.querySelector('[name="start"]');
    const end = leaveForm.querySelector('[name="end"]');
    const error = leaveForm.querySelector('.form-error');
    if (start.value && end.value && end.value < start.value) {
      event.preventDefault(); error.style.display = 'block'; error.textContent = 'The end date must be on or after the start date.'; end.focus();
    }
  });

  document.querySelectorAll('[data-confirm]').forEach(link => link.addEventListener('click', event => {
    if (!window.confirm(link.dataset.confirm)) event.preventDefault();
  }));
});
