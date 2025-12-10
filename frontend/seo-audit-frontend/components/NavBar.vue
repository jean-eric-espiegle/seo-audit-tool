<template>
	<nav class="navbar">
		<div class="links">
			<NuxtLink to="/">Home</NuxtLink>
			<NuxtLink to="/compare">Compare</NuxtLink>
		</div>

		<button class="toggle-btn" type="button" @click="toggleDarkMode">
			{{ darkMode ? 'Light Mode' : 'Dark Mode' }}
		</button>
	</nav>
</template>

<script setup>
const { darkMode, toggleDarkMode } = useDarkMode();
</script>

<style scoped>
.navbar {
	width: 100%;
	background: var(--card-bg);
	box-shadow: 0px 2px 15px var(--card-shadow);
	padding: 14px 24px;
	border-radius: 14px;
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 40px;
	position: sticky;
	top: 16px;
	z-index: 20;
}

.links {
	display: flex;
	align-items: center;
	gap: 18px;
}

a {
	text-decoration: none;
	color: var(--text);
	font-weight: 600;
}

a.router-link-active {
	color: var(--primary);
}

.toggle-btn {
	background: var(--input-bg);
	border: 1px solid var(--border);
	color: var(--text);
	padding: 8px 16px;
	font-size: 14px;
	border-radius: 10px;
	cursor: pointer;
	transition: 0.2s ease;
}

.toggle-btn:hover {
	background: var(--border);
}
</style>
