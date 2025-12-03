export default defineNuxtConfig({
  devtools: { enabled: true },

  // Enable SSR (default)
  ssr: true,

  modules: ["@nuxtjs/tailwindcss"],

  css: ["~/assets/css/tailwind.css"],

  app: {
    head: {
      title: "SEO Audit Tool",
    },
  },
})
