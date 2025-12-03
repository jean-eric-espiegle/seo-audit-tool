// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: ["@nuxtjs/tailwindcss"],

  css: ["~/assets/css/tailwind.css"],   // This now works

  app: {
    head: {
      title: "SEO Audit Tool",
    },
  },
})
