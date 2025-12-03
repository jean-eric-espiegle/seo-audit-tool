export default defineNuxtConfig({
  modules: ["@nuxtjs/tailwindcss"],
  css: ["~/assets/css/tailwind.css"],
// devtools: { enabled: true },
  nitro: {
    preset: "netlify",
    serveStatic: true, // 👈 THIS FIXES THE MISSING BUILD FOLDER
  },

  build: {
    transpile: ["@nuxtjs/tailwindcss"]
  }
});
