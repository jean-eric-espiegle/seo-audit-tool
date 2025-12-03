export default defineNuxtConfig({
  devtools: { enabled: true },

  ssr: false, // TURN OFF SSR – IMPORTANT
  nitro: {
    preset: "netlify-static"  // USE STATIC GENERATION
  },

  modules: ["@nuxtjs/tailwindcss"],
  css: ["~/assets/css/tailwind.css"],

  app: {
    head: {
      title: "SEO Audit Tool",
    }
  }
});
