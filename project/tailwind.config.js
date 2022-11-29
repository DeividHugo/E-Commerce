/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
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
