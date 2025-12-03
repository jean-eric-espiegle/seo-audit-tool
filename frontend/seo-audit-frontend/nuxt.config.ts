export default defineNuxtConfig({
  ssr: false, // ⬅ SPA mode (important!)

  app: {
    baseURL: '/',
  },

  css: [
    '~/assets/css/tailwind.css'
  ],

  modules: [
    '@nuxtjs/tailwindcss'
  ]
});
