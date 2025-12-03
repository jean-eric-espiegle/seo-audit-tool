export default defineNuxtConfig({
  ssr: false,

  app: {
    baseURL: '/',
  },

  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  },

  nitro: {
    preset: 'static'
  }
});
