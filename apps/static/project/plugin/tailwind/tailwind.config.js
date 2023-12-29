tailwind.config = {
  darkMode:'class',
  theme: {
    screens:{
      xs: '480px',
      sm:'640px',
      md:'768px',
      lg:'1024px',
      xl:'1280px',
    },
    container: {
      padding: {
        DEFAULT: '20px',
        sm: '0.9rem',
        lg: '1rem',
        xl: '1.2rem'
      },
      center: 'true',
    },
    fontFamily: {
      'montserrat': 'Montserrat',
      'elmessiri': 'El-Messiri',
      'czizh': 'Czizh',
    },
    letterSpacing: {
      widest: '.72px',
    },
    extend: {
      colors: {
        'dark': '#363435',
        'violet': '#A368AA',
        'light': '#FDF9F6',
      },
      fontWeight:{
        lighter: '275'
      },
      lineHeight: {
        'lg': '1.5rem',
        'base': '1.25rem',
      },
    }
  },
};