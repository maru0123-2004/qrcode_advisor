export const $APIError = {
	properties: {
		status_code: {
			type: 'number',
			default: 400
		},
		detail: {
			type: 'string',
			default: 'Something Wrong'
		}
	}
} as const;

export const $Body_Auth_signin = {
	properties: {
		grant_type: {
			type: 'any-of',
			contains: [
				{
					type: 'string',
					pattern: 'password'
				},
				{
					type: 'null'
				}
			]
		},
		username: {
			type: 'string',
			isRequired: true
		},
		password: {
			type: 'string',
			isRequired: true
		},
		scope: {
			type: 'string',
			default: ''
		},
		client_id: {
			type: 'any-of',
			contains: [
				{
					type: 'string'
				},
				{
					type: 'null'
				}
			]
		},
		client_secret: {
			type: 'any-of',
			contains: [
				{
					type: 'string'
				},
				{
					type: 'null'
				}
			]
		}
	}
} as const;

export const $Forbidden = {
	properties: {
		status_code: {
			type: 'number',
			default: 401
		},
		detail: {
			type: 'string',
			default: 'Not authenticated'
		}
	}
} as const;

export const $HTTPValidationError = {
	properties: {
		detail: {
			type: 'array',
			contains: {
				type: 'ValidationError'
			}
		}
	}
} as const;

export const $NotFound = {
	properties: {
		status_code: {
			type: 'number',
			default: 404
		},
		detail: {
			type: 'string',
			default: 'Not found'
		}
	}
} as const;

export const $Operator = {
	properties: {
		id: {
			type: 'string',
			isRequired: true
		},
		name: {
			type: 'string',
			isRequired: true
		}
	}
} as const;

export const $StopData = {
	properties: {
		stop_id: {
			type: 'string',
			isRequired: true,
			format: 'uuid'
		},
		name: {
			type: 'string',
			isRequired: true
		},
		position: {
			type: 'any-of',
			contains: [
				{
					type: 'array',
					contains: {
						type: 'number'
					}
				},
				{
					type: 'null'
				}
			],
			isRequired: true
		},
		distance: {
			type: 'number'
		}
	}
} as const;

export const $Token = {
	properties: {
		access_token: {
			type: 'string',
			isRequired: true
		},
		token_type: {
			type: 'string',
			default: 'bearer'
		},
		user_id: {
			type: 'string',
			isRequired: true,
			format: 'uuid'
		},
		expired_in: {
			type: 'string',
			isRequired: true,
			format: 'date-time'
		}
	}
} as const;

export const $User = {
	properties: {
		id: {
			type: 'string',
			isRequired: true,
			format: 'uuid'
		},
		name: {
			type: 'string',
			isRequired: true
		},
		mail: {
			type: 'string',
			isRequired: true,
			format: 'email'
		}
	}
} as const;

export const $UserCreate = {
	properties: {
		name: {
			type: 'string',
			isRequired: true,
			maxLength: 1024
		},
		mail: {
			type: 'string',
			isRequired: true,
			format: 'email'
		},
		password: {
			type: 'string',
			isRequired: true,
			format: 'password'
		}
	}
} as const;

export const $ValidationError = {
	properties: {
		loc: {
			type: 'array',
			contains: {
				type: 'any-of',
				contains: [
					{
						type: 'string'
					},
					{
						type: 'number'
					}
				]
			},
			isRequired: true
		},
		msg: {
			type: 'string',
			isRequired: true
		},
		type: {
			type: 'string',
			isRequired: true
		}
	}
} as const;
