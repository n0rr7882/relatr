import { Injectable } from '@angular/core';
import { Store } from './store';
import { RelatrState } from './relatr-state';

@Injectable()
export class RelatrStore extends Store<RelatrState> {

}