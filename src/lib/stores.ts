import { writable } from 'svelte/store';

export const hideNav = writable<boolean>(false);
export const theme = writable('light');
export const backgroundColor = writable('#ffffff');

type language = 'en' | 'ru';
export const lang = writable<language>('en');
