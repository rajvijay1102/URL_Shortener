document.addEventListener('DOMContentLoaded', () => {
  const colorWheel = document.querySelector('.color-wheel');
  const numSpans = 5;

  for (let i = 0; i < numSpans; i++) {
    const span = document.createElement('span');
    const size = 100 + Math.random() * 50;
    const left = Math.random() * (100 - size) + '%';
    const top = Math.random() * (100 - size) + '%';
    const angle = Math.random() * 360;

    span.style.width = `${size}px`;
    span.style.height = `${size}px`;
    span.style.left =left;
    span.style.top = top;
    span.style.transform = `rotate(${angle}deg) translate(-50%, -50%)`;

    colorWheel.appendChild(span);
  }
});