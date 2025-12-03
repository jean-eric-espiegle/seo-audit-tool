// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: true },
  nitro: {
  preset: "netlify",
  output: {
    publicDir: ".netlify/publish"
  }
  },

  modules: ["@nuxtjs/tailwindcss"],

  css: ["~/assets/css/tailwind.css"],   // This now works

  app: {
    head: {
      title: "SEO Audit Tool",
    },
  },
})
