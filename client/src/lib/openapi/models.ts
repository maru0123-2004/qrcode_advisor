export type APIError = {
	status_code?: number;
	detail?: string;
};

export type Body_Auth_signin = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};

export type Forbidden = {
	status_code?: number;
	detail?: string;
};

export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};

export type NotFound = {
	status_code?: number;
	detail?: string;
};

export type StopData = {
	stop_id: string;
	name: string;
	pole_number: string;
};

export type Token = {
	access_token: string;
	token_type?: string;
	user_id: string;
	expired_in: string;
};

export type User = {
	id: string;
	name: string;
	mail: string;
};

export type UserCreate = {
	name: string;
	mail: string;
	password: string;
};

export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};
