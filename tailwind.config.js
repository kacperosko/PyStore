/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content:  [
      './apps/_templates/**/*.{html,js}',
      './apps/_static/Typescript/*.{ts, js}'
  ],
  theme: {
    extend: {
      colors:{
        'lime': '#4ECCA3',
        'dark-lime': '#3ea382',
        'pink': '#F2668B',
        'white': '#EEEEEE',
        'neutral-white': '#FFFFFF',
        'dark': '#393E46',
        'light-dark': '#4d5159',
        'dark-xl': '#2e3238',
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
        '200': '45rem',
        '300': '60rem',
      },
      fontSize: {
        '2xs': ['0.5rem', {
        lineHeight: '1rem',
        letterSpacing: '-0.01em',
        fontWeight: '500',
      }],
      },
      minWidth: {
        '8': '2rem',
      },
      maxHeight: {
        '9/10': '90vh',
        '8/10': '80vh'
      },
      maxWidth: {
        "52": '13rem',
        "60": '15rem'
      },
      borderRadius: {
        "1/2": '50%'
      }
    },
  },
  plugins: [],
}