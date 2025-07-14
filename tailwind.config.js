const colors = require('tailwindcss/colors')
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['*.html', '_site/*.html','_site/**/*.html', '_pages/**/*.md', '_posts/**/*.md', '_layouts/**/*.html', '_includes/**/*.html'],
  theme: {
    extend: {
      colors: {
        gray: colors.slate,
        primary: colors.rose,
        secondary: colors.indigo,
        tertiary: colors.slate,
        danger: colors.red,
        white: "#FAFAFA",
        black: "#2E2E2E",
        'main': {
          50: '#F3F8F9',
          100: '#B8D2D9',
          200: '#7DADBA',
          300: '#41879A',
          400: '#126981',
          500: '#0F576B',
          600: '#0D4B5C',
          700: '#0B3E4C',
          800: '#08313D',
          900: '#06252D',
          950: '#04181E',
        },
        'accent': {
          50: '#FFFBF6',
          100: '#FFE4CB',
          200: '#FFCEA0',
          300: '#FFB775',
          400: '#FFA552',
          500: '#D48944',
          600: '#B5753A',
          700: '#966130',
          800: '#784E27',
          900: '#593A1D',	
          950: '#3B2613',
        },
        'sub': {
          50: '#F8FBFC',	
          100: '#D4E7EE',
          200: '#B0D2E0',
          300: '#8CBED1',
          400: '#6FAEC6',
          500: '#5C90A4',
          600: '#4F7C8D',
          700: '#416775',
          800: '#34525D',
          900: '#273D45',
          950: '#1A282E',
        },
      },
      fontFamily: {
        sans: ['Work Sans', 'Inter var', ...defaultTheme.fontFamily.sans]
      }
    }
  },
  variants: {
    extend: {},
    fill: ['hover', 'focus']
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio')
  ]
}
