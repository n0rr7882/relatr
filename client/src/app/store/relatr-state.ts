import { IChain, IAccount, IAppState } from './interfaces';

export class RelatrState implements IAppState {
    chains: IChain[] = [];
    offset: number = 0;
    selected: number = null;
    loading: boolean = false;
}