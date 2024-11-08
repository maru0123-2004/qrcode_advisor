<script lang="ts">
	import { Scanner } from "qrcode-scanner-svelte";
    let result:string|null=null;
</script>
<Scanner bind:result>
    {#if result}
			<div>
				The result is: {result}
			</div>
			<div>
				<button on:click={() => (result = null)}>Scan again</button>
			</div>
	{/if}
</Scanner>