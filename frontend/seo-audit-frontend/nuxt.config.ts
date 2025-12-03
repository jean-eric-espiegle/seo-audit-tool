// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: 'netlify'
  },

  devtools: { enabled: false },

  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  }
})
