// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: true },
  nitro: {
    preset: "netlify"
  },

  modules: ["@nuxtjs/tailwindcss"],

  css: ["~/app/assets/css/tailwind.css"],   // This now works

  app: {
    head: {
      title: "SEO Audit Tool",
    },
  },
})
