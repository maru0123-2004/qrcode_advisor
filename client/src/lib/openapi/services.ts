import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Body_Auth_signin, Token, User, UserCreate, StopData, Operator } from './models';

export type AuthData = {
	AuthSignin: {
		formData: Body_Auth_signin;
	};
	AuthSignup: {
		requestBody: UserCreate;
	};
};

export type SearchData = {
	SearchSearch: {
		searchWord: string;
	};
	SearchSearchPosition: {
		lat: number;
		long: number;
	};
};

export type CheckStopData = {
	CheckStopCheckStop: {
		destId: string;
		qrdata: string;
	};
};

export type AdminData = {};

export class AuthService {
	/**
	 * Signin
	 * @returns Token Successful Response
	 * @throws ApiError
	 */
	public static authSignin(data: AuthData['AuthSignin']): CancelablePromise<Token> {
		const { formData } = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/auth/signin',
			formData: formData,
			mediaType: 'application/x-www-form-urlencoded',
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Signup
	 * @returns User Successful Response
	 * @throws ApiError
	 */
	public static authSignup(data: AuthData['AuthSignup']): CancelablePromise<User> {
		const { requestBody } = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/auth/signup',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Signout
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static authSignout(): CancelablePromise<unknown> {
		return __request(OpenAPI, {
			method: 'POST',
			url: '/auth/signout',
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`
			}
		});
	}

	/**
	 * Session
	 * @returns Token Successful Response
	 * @throws ApiError
	 */
	public static authSession(): CancelablePromise<Array<Token>> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/auth/session',
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`
			}
		});
	}
}

export class SearchService {
	/**
	 * Search
	 * @returns StopData Successful Response
	 * @throws ApiError
	 */
	public static searchSearch(data: SearchData['SearchSearch']): CancelablePromise<Array<StopData>> {
		const { searchWord } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/',
			query: {
				search_word: searchWord
			},
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Search Position
	 * @returns StopData Successful Response
	 * @throws ApiError
	 */
	public static searchSearchPosition(
		data: SearchData['SearchSearchPosition']
	): CancelablePromise<Array<StopData>> {
		const { lat, long } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/position',
			query: {
				lat,
				long
			},
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}
}

export class CheckStopService {
	/**
	 * Checkstop
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static checkStopCheckStop(
		data: CheckStopData['CheckStopCheckStop']
	): CancelablePromise<boolean> {
		const { destId, qrdata } = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/checkstop/',
			query: {
				dest_id: destId,
				qrdata
			},
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}
}

export class AdminService {
	/**
	 * Companies
	 * @returns Operator Successful Response
	 * @throws ApiError
	 */
	public static adminCompanies(): CancelablePromise<Array<Operator>> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/admin/companies',
			errors: {
				400: `Bad Request`,
				401: `Unauthorized`,
				404: `Not Found`
			}
		});
	}
}
