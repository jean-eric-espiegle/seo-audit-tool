// nuxt.config.ts
export default defineNuxtConfig({
  ssr: false,

  app: {
    head: {
      title: "SEO Audit Tool",
      meta: [{ name: "viewport", content: "width=device-width, initial-scale=1" }]
    }
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || "https://seo-audit-tool-production-a57e.up.railway.app"
    }
  }
});
