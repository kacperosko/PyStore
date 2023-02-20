/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content:  ['./apps/templates/**/*.{html,js}'],
  theme: {
    extend: {
      colors:{
        'lime': '#4ECCA3',
        'dark-lime': '#3ea382',
        'pink': '#F2668B',
        'white': '#EEEEEE',
        'neutral-white': '#FFFFFF',
        'dark': '#393E46',
      },
      lineHeight: {
        '12': '3rem',
      },
      letterSpacing: {
        'super-wide': '0.3rem',
      },
      borderRadius: {
        'xl': '20px',
      },
      height: {
        '150': '30rem',
      },
      width: {
        '150': '30rem',
      },
      fontSize: {
        '2xs': ['0.5rem', {
        lineHeight: '1rem',
        letterSpacing: '-0.01em',
        fontWeight: '500',
      }],
      }
    },
  },
  plugins: [],
}