export interface IAppState {
    chains: IChain[];
    offset: number;
    selected: number;
    loading: boolean;
}

export interface IUser {
    id: number;
    thumbnail: string;
    banner: string;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    date_joined: Date;
}

export interface IAccount {
    id: number;
    user: IUser;
    thumbnail: string;
    banner: string;
    created_at: Date;
}

export interface ITag {
    id: number;
    name: string;
}

export interface IChain {
    id: number;
    account: IAccount;
    text: string;
    image: string;
    tags: ITag[];
    mentions: IAccount[];
    likes: IAccount[];
    parent_chain: IChain | number;
    child_chains: IChain[];
    created_at: Date;
}