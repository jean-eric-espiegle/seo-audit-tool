export default defineNuxtConfig({
  ssr: false,   // disable server-side rendering (SPA mode)

  app: {
    baseURL: '/',
    buildAssetsDir: '/_nuxt/'
  },

  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  },

  // ensure SPA behaviour for Netlify
  routeRules: {
    '/**': { prerender: false }
  },

  nitro: {
    preset: 'static',   // ⬅ correct preset for static output in Nuxt 4
  }
});
