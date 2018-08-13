import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { ButtonsModule } from 'ngx-bootstrap/buttons';
import { TypeaheadModule } from 'ngx-bootstrap/typeahead';
import { AlertModule } from 'ngx-bootstrap/alert';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { ModalModule } from 'ngx-bootstrap/modal';
import { TooltipModule } from 'ngx-bootstrap/tooltip';
import { ProgressbarModule } from 'ngx-bootstrap/progressbar';

import { AppComponent } from './app.component';

// pages
import { TimelineComponent } from './pages/timeline/timeline.component';
import { ChainDetailComponent } from './pages/chain-detail/chain-detail.component';

// components
import { NavComponent } from './components/nav/nav.component';
import { ChainComponent } from './components/chain/chain.component';
import { ExtendedChainComponent } from './components/extended-chain/extended-chain.component';

// utils
import { ThumbComponent } from './utils/thumb/thumb.component';
import { ClipComponent } from './utils/clip/clip.component';


@NgModule({
  declarations: [
    AppComponent,

    // pages
    TimelineComponent,
    ChainDetailComponent,

    // components
    NavComponent,
    ChainComponent,
    ExtendedChainComponent,

    // utils
    ThumbComponent,
    ClipComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule,

    // bootstrap
    ButtonsModule.forRoot(),
    TypeaheadModule.forRoot(),
    AlertModule.forRoot(),
    BsDropdownModule.forRoot(),
    ModalModule.forRoot(),
    TooltipModule.forRoot(),
    ProgressbarModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
