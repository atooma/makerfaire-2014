package com.atooma.plugin.chickenfoot;

import android.content.Context;

import com.atooma.plugin.Module;

public class CHICKENFOOT extends Module {

	public static final String MODULE_ID = "CHICKENFOOT";
	public static final int MODULE_VERSION = 1;

	public CHICKENFOOT(Context context, String id, int version) {
		super(context, id, version);
	}

	@Override
	public void registerComponents() {
		registerPerformer(new PE_BEEP(getContext(), "BEEP", 1));

		registerPerformer(new PE_LIGHTS_ON(getContext(), "LIGHTSON", 1));
		registerPerformer(new PE_LIGHTS_OFF(getContext(), "LIGHTSOFF", 1));

		registerPerformer(new PE_FORWARD(getContext(), "FORWARD", 1));
		registerPerformer(new PE_BACK(getContext(), "BACK", 1));
		registerPerformer(new PE_LEFT(getContext(), "LEFT", 1));
		registerPerformer(new PE_RIGHT(getContext(), "RIGHT", 1));

	}

	@Override
	public void defineUI() {
		setIcon(R.drawable.plugin_icon_normal);
		setTitle(R.string.module_name);
	}

	@Override
	public void defineAuth() {
		//Get the username autenticated from activity and define it with setAuthenticated(true, authText);
	}

	@Override
	public void clearCredentials() {
		//Clear
	}

}