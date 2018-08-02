import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExtendedChainComponent } from './extended-chain.component';

describe('ExtendedChainComponent', () => {
  let component: ExtendedChainComponent;
  let fixture: ComponentFixture<ExtendedChainComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExtendedChainComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExtendedChainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
