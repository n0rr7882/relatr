import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChainDetailComponent } from './chain-detail.component';

describe('ChainDetailComponent', () => {
  let component: ChainDetailComponent;
  let fixture: ComponentFixture<ChainDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChainDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChainDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
