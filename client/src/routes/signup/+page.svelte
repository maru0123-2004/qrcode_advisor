<script lang="ts">
	import { AuthService } from "$lib/openapi";
    import Button from "flowbite-svelte/Button.svelte";
    import Card from "flowbite-svelte/Card.svelte";
    import Heading from "flowbite-svelte/Heading.svelte";
    import Input from "flowbite-svelte/Input.svelte";
    import Label from "flowbite-svelte/Label.svelte";
	import { goto } from "$app/navigation";
    
    let username="";
    let password="";
    let mail="";
    const onSubmit=async (e:SubmitEvent) => {
        e.preventDefault()
        await AuthService.authSignup({requestBody:{name:username, password, mail}});
        username="";
        password="";
        mail="";
        goto("/signin");
    }
</script>

<Card class="mx-auto">
    <Heading tag="h3">サインアップ</Heading>
    <form on:submit={onSubmit} class="space-y-2 flex flex-col">
            <Label for="username">User Name</Label>
            <Input id="username" type="text" bind:value={username} required />
            <Label for="mail">Email Address</Label>
            <Input id="mail" type="email" bind:value={mail} required />
            <Label for="password">Password</Label>
            <Input id="password" type="password" bind:value={password} required />
            <Button type="submit">Sign up</Button>
    </form>
</Card>