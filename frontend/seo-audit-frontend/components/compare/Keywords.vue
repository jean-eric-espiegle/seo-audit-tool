<template>
	<section class="card table-card">
		<div class="section-header">
			<h2>Keywords</h2>
		</div>
		<div class="two-col">
			<div>
				<p class="eyebrow">Primary</p>
				<h4 class="site-title">{{ mainUrl }}</h4>
				<div class="tags">
					<span v-for="kw in mainKeywords || []" :key="kw.keyword" class="tag">
						{{ kw.keyword }} ({{ kw.count }})
					</span>
				</div>
			</div>
			<div>
				<p class="eyebrow">Competitor</p>
				<h4 class="site-title">{{ competitorUrl }}</h4>
				<div class="tags">
					<span v-for="kw in competitorKeywords || []" :key="kw.keyword" class="tag">
						{{ kw.keyword }} ({{ kw.count }})
					</span>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup>
defineProps({
	mainUrl: String,
	competitorUrl: String,
	mainKeywords: Array,
	competitorKeywords: Array,
});
</script>

<style scoped>
.section-header h2 {
	margin-bottom: 12px;
}

.two-col {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
	gap: 16px;
}

.tags {
	display: flex;
	flex-wrap: wrap;
	gap: 12px;
}

@media (max-width: 720px) {
	.two-col {
		grid-template-columns: 1fr;
	}
}
</style>
