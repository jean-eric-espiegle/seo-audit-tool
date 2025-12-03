export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],

  css: [
    '~/assets/css/tailwind.css'
  ],

//   devtools: { enabled: true },

  build: {
    transpile: []
  }
})
