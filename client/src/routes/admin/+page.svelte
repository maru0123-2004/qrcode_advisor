<script lang="ts">
	import A from "flowbite-svelte/A.svelte";
    import type { PageData } from "./$types";
	import { Label, Select, Input, Card } from "flowbite-svelte";
	import { AdminService } from "$lib/openapi";
    import QrCode from "svelte-qrcode";
    export let data:PageData;
    const user=data.user;
    let operator:null|string=null;
    let busnum:null|string=null;
</script>

{#if !$user}
    このページを使用するには、<A href="/signin"> サインイン</A>が必要です。<br />
    アカウントをお持ちでない場合は、<A href="/signup">サインアップ</A>してください
{:else}
    
    {#await AdminService.adminCompanies()}
        事業者情報を取得しています...
    {:then operators}
        <Label for="operators">事業者選択</Label>
        <Select id="operators" items={operators.map((op)=>{return {name:op.name, value:op.id}})} bind:value={operator} />
    {/await}
    {#if operator}
        <Label for="busnum">バスナンバー入力</Label>
        <Input id="busnum" type="text" bind:value={busnum} />
    {/if}
    {#if busnum}
        <Card>
            <QrCode value={operator+"."+busnum} />
        </Card>
    {/if}
{/if}