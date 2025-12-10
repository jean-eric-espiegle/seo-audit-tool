<template>
	<div class="grid grid-2 metrics-grid">
		<div class="card"><strong>Title:</strong> {{ result.title }}</div>
		<div class="card">
			<strong>Description:</strong> {{ result.meta_description }}
		</div>
		<div class="card"><strong>H1:</strong> {{ result.h1 }}</div>
		<div class="card">
			<strong>Word Count:</strong> {{ result.word_count }}
		</div>
		<div class="card">
			<strong>Internal Links:</strong> {{ result.internal_links }}
		</div>
		<div class="card">
			<strong>External Links:</strong> {{ result.external_links }}
		</div>
		<div class="card">
			<strong>Missing ALTs:</strong>
			<span :class="result.missing_image_alts > 0 ? 'bad' : 'good'">
				{{ result.missing_image_alts }}
			</span>
		</div>
		<div class="card">
			<strong>Viewport Meta:</strong> {{ result.has_viewport_tag }}
		</div>
		<div class="card">
			<strong>Robots.txt:</strong> {{ result.robots_txt_found }}
		</div>
		<div class="card">
			<strong>Sitemap:</strong> {{ result.sitemap_found }}
		</div>
	</div>
</template>

<script setup>
defineProps({
	result: {
		type: Object,
		required: true,
	},
});
</script>

<style scoped>
.metrics-grid {
	margin-bottom: 30px;
}
</style>
