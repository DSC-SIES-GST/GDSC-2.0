/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./dist/*.html'],
  theme: {
    screens:{
      sm:'480px',
      md: '768px',
      lg:'976px',
      xl:'1440px'
    },
    extend: {
      colors:{
        linear_org: 'hsl(0,100,67,100%)',
        linear_prl: 'hsl(281,94,70,100%)',
        linear_ylw: 'hsl(44,100,81,100%)',
        linear_yel: 'hsl(40,100,66,100%)',
        black: '#000',        
        white: '#fff'      
      }
    },
  },
  plugins: [],
}
