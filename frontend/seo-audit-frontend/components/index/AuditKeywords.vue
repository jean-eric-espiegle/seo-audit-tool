<template>
	<div class="card" v-if="keywords && keywords.length">
		<h2 class="title">Top Keywords</h2>

		<div class="tags">
			<span class="tag" v-for="item in keywords" :key="item.keyword">
				{{ item.keyword }} ({{ item.count }})
			</span>
		</div>
	</div>
</template>

<script setup>
defineProps({
	keywords: {
		type: Array,
		default: () => [],
	},
});
</script>

<style scoped>
.title {
	font-size: 22px;
	margin-bottom: 18px;
}

.tags {
	display: flex;
	flex-wrap: wrap;
	gap: 12px;
}
</style>
