/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    "./src/**/*.{html,js}",
    './node_modules/flowbite/**/*.js'
],
  theme: {
    colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'default': '#2196F3',
        },
    extend: {},
  },
    plugins: [
        require('flowbite/plugin')
    ]
,
}
