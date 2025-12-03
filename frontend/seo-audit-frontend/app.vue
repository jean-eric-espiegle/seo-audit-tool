<template>
	<NuxtLayout>
		<NuxtPage />
	</NuxtLayout>
</template>

<script setup>
useHead({
	link: [
		{
			rel: 'stylesheet',
			href: 'https://cdn.jsdelivr.net/npm/tailwindcss@3.4.4/dist/tailwind.min.css',
		},
	],
});
</script>
